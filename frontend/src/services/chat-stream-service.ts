export async function streamMessage(

  sessionId: number,

  content: string,

  token: string,

  onChunk: (chunk: string) => void

) {

  const response =
    await fetch(

      `http://localhost:8000/chat/sessions/${sessionId}/stream`,

      {

        method: "POST",

        headers: {

          Authorization:
            `Bearer ${token}`,

          "Content-Type":
            "application/json",

          Accept:
            "text/event-stream"

        },

        body: JSON.stringify({

          content

        })

      }

    );

  console.log(
    "STREAM RESPONSE:",
    response.status
  );

  if (!response.ok) {

    throw new Error(

      `Streaming failed: ${response.status}`

    );
  }

  const reader =
    response.body?.getReader();

  if (!reader) {

    console.error(
      "No response body"
    );

    return;
  }

  const decoder =
    new TextDecoder();

  while (true) {

    const {

      value,

      done

    } =
      await reader.read();

    if (done) {

      console.log(
        "STREAM FINISHED"
      );

      break;
    }

    const chunk =
      decoder.decode(
        value,
        {
          stream: true
        }
      );

    console.log(
      "CHUNK RECEIVED:",
      chunk
    );

    onChunk(
      chunk
    );
  }
}
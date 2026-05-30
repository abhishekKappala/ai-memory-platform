import { api } from "./api";

export async function getSessions() {

  const response =
    await api.get(
      "/chat/sessions"
    );

  return response.data;
}

export async function getMessages(
  sessionId:number
) {

  const response =
    await api.get(
      `/chat/sessions/${sessionId}/messages`
    );

  return response.data;
}

export async function createSession() {

  const response =
    await api.post(

      "/chat/sessions",

      {
        title: "New Chat"
      }

    );

  return response.data;
}

export async function sendMessage(

  sessionId:number,

  content:string

) {

  const response =
    await api.post(

      `/chat/sessions/${sessionId}/messages`,

      {
        content
      }

    );
  return response.data;
}
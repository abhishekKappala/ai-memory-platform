"use client";

import { ChatBubble } from "./message-bubble";

import { useChatStore } from "@/store/chat-store";

import { useChat } from "../hooks/use-chat";

import { ChatMessage } from "../types/chat";

export function ChatMessages() {

  const sessionId =
    useChatStore(
      (s) => s.activeSessionId
    );

  const {

    data: messages = [],

    isLoading,

    isError,

  } = useChat(
    sessionId
  );

  if (!sessionId) {

    return (

      <div

        className="
        flex-1
        flex
        items-center
        justify-center
        text-muted-foreground
      "

      >

        Select a chat to begin

      </div>
    );
  }

  if (isLoading) {

    return (

      <div

        className="
        flex-1
        flex
        items-center
        justify-center
      "

      >

        Loading messages...

      </div>
    );
  }

  if (isError) {

    return (

      <div

        className="
        flex-1
        flex
        items-center
        justify-center
        text-red-500
      "

      >

        Failed to load messages

      </div>
    );
  }

  return (

    <div

      className="
      flex-1
      overflow-y-auto
      px-6
      py-8
      space-y-6
    "

    >

      {messages.length === 0 && (

        <div

          className="
          text-center
          text-muted-foreground
          mt-20
        "

        >

          Start a conversation

        </div>

      )}

      {messages.map(

        (message: ChatMessage) => (

          <ChatBubble

            key={message.id}

            role={message.role}

            content={message.content}

          />

        )

      )}

    </div>
  );
}
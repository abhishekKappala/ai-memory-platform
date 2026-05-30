"use client";

import { useState } from "react";
import { Send } from "lucide-react";

import { useSendMessage } from "../hooks/use-send-message";
import { useChatStore } from "@/store/chat-store";

export function ChatInput() {

  const [message, setMessage] =
    useState("");

  const sessionId =
    useChatStore(
      (s) => s.activeSessionId
    );

  const mutation =
    useSendMessage();

  async function handleSend() {

    const trimmed =
      message.trim();

    if (!trimmed) return;

    if (!sessionId) return;

    mutation.mutate({

      sessionId,

      content: trimmed,

    });

    setMessage("");
  }

  const handleKeyDown = (
    e: React.KeyboardEvent<HTMLTextAreaElement>
  ) => {

    if (

      e.key === "Enter"

      &&

      !e.shiftKey

    ) {

      e.preventDefault();

      handleSend();
    }
  };

  return (

    <div

      className="
      border-t
      p-5
    "

    >

      <div

        className="
        mx-auto
        flex
        max-w-4xl
        items-end
        gap-3
        rounded-2xl
        border
        p-3
        shadow-sm
      "

      >

        <textarea

          value={message}

          onChange={(e) =>
            setMessage(
              e.target.value
            )
          }

          onKeyDown={
            handleKeyDown
          }

          rows={1}

          placeholder="Message AI..."

          disabled={
            mutation.isPending
          }

          className="
          flex-1
          resize-none
          bg-transparent
          outline-none
          text-sm
          disabled:opacity-50
        "

        />

        <button

          onClick={handleSend}

          disabled={
            mutation.isPending
          }

          className="
          rounded-xl
          p-2
          hover:bg-muted
          disabled:opacity-50
        "

        >

          <Send size={18} />

        </button>

      </div>

    </div>
  );
}
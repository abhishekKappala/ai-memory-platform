"use client";

import { Sidebar } from "./sidebar";
import { ChatWindow } from "./chat-window";

export function ChatLayout() {

  return (
    <div className="flex h-screen bg-background text-foreground">

      <Sidebar />

      <ChatWindow />

    </div>
  );
}
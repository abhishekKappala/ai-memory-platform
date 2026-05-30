"use client";

import {

  ChatMessages

} from "./chat-messages";

import {

  ChatInput

} from "./chat-input";

export function ChatWindow(){

  return(

    <main

      className="

      flex-1

      flex

      flex-col

    "

    >

      <ChatMessages />

      <ChatInput />

    </main>
  );
}
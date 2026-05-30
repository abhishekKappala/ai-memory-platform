"use client";

import ReactMarkdown
from "react-markdown";

import remarkGfm
from "remark-gfm";

export function ChatBubble({

  role,

  content

}:{

  role:string;

  content:string;

}){

  const isUser=
    role==="user";

  return(

    <div

      className={`

      flex

      ${

        isUser

        ?

        "justify-end"

        :

        "justify-start"

      }

      `}

    >

      <div

        className={`

        max-w-[75%]

        rounded-2xl

        px-5

        py-4

        text-sm

        leading-7

        shadow-sm

        ${

          isUser

          ?

          "bg-white text-black"

          :

          "bg-muted"

        }

        `}

      >

        <ReactMarkdown

          remarkPlugins={[

            remarkGfm
          ]}

        >

          {content}

        </ReactMarkdown>

      </div>

    </div>
  );
}
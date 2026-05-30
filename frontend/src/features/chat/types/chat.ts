export interface ChatMessage {

  id: number;

  content: string;

  created_at: string;

  session_id: number;

  role:
    | "user"
    | "assistant";
}

export interface ChatSession {

  id: number;

  title: string;

  created_at: string;
}
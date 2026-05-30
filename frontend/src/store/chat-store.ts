import { create } from "zustand";

interface ChatStore {

  activeSessionId:
    number | null;

  setActiveSession:
    (
      id: number
    ) => void;
}

export const useChatStore =
  create<ChatStore>((set) => ({

    activeSessionId: null,

    setActiveSession: (id) =>

      set({

        activeSessionId: id,

      }),

  }));
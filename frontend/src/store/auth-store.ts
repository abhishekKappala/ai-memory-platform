import { create } from "zustand";

interface AuthStore {

  token: string | null;

  hydrated: boolean;

  setToken: (token: string) => void;

  loadToken: () => void;

  logout: () => void;
}

export const useAuthStore =
  create<AuthStore>((set) => ({

    token: null,

    hydrated: false,

    setToken: (token) => {

      localStorage.setItem(
        "token",
        token
      );

      set({ token });
    },

    loadToken: () => {

      const token =
        localStorage.getItem(
          "token"
        );

      set({

        token,

        hydrated: true
      });
    },

    logout: () => {

      localStorage.removeItem(
        "token"
      );

      set({

        token: null
      });
    }
}));
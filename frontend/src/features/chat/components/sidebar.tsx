"use client";
import { useEffect } from "react";
import { MessageSquare, Plus, LogOut } from "lucide-react";
import { useRouter } from "next/navigation";
import { useSessions } from "../hooks/use-sessions";
import { useChatStore } from "@/store/chat-store";
import { useAuthStore } from "@/store/auth-store";
import { createSession } from "@/services/chat-service";
import type { ChatSession } from "../types/chat";

export function Sidebar() {
  const { data: sessions = [], isLoading } = useSessions();
  const activeSessionId = useChatStore((s) => s.activeSessionId);
  const setActiveSession = useChatStore((s) => s.setActiveSession);
  const logout = useAuthStore((s) => s.logout);
  const router = useRouter();

  useEffect(() => {
    if (sessions.length > 0 && !activeSessionId) {
      setActiveSession(sessions[0].id);
    }
  }, [sessions, activeSessionId, setActiveSession]);

  async function handleNewChat() {
    try {
      const session = await createSession();
      setActiveSession(session.id);
    } catch (error) {
      console.error("Failed to create session", error);
    }
  }

  function handleLogout() {
    logout();
    router.push("/login");
  }

  return (
    <aside className="w-[280px] border-r flex flex-col bg-muted/30">
      <div className="p-4 border-b">
        <button
          onClick={handleNewChat}
          className="w-full flex items-center gap-2 rounded-lg border p-3 hover:bg-muted transition-colors"
        >
          <Plus size={18} />
          New Chat
        </button>
      </div>

      <div className="flex-1 overflow-y-auto p-3 space-y-2">
        {isLoading && (
          <div className="text-sm text-muted-foreground px-3 py-2">
            Loading sessions...
          </div>
        )}
        {!isLoading && sessions.length === 0 && (
          <div className="text-sm text-muted-foreground px-3 py-2">
            No chats yet
          </div>
        )}
        {sessions.map((session: ChatSession) => (
          <button
            key={session.id}
            onClick={() => setActiveSession(session.id)}
            className={`
              w-full flex items-center gap-3 rounded-lg px-3 py-3
              text-sm transition-colors text-left
              ${activeSessionId === session.id ? "bg-muted" : "hover:bg-muted"}
            `}
          >
            <MessageSquare size={16} />
            <span className="truncate flex-1">{session.title}</span>
          </button>
        ))}
      </div>

      <div className="p-4 border-t">
        <button
          onClick={handleLogout}
          className="w-full flex items-center gap-2 rounded-lg px-3 py-3 text-sm hover:bg-muted transition-colors text-muted-foreground hover:text-foreground"
        >
          <LogOut size={18} />
          Logout
        </button>
      </div>
    </aside>
  );
}
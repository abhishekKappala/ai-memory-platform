import { useQuery } from "@tanstack/react-query";

import { getMessages } from "@/services/chat-service";

export function useChat(
  sessionId: number | null
) {
  return useQuery({

    queryKey: [
      "messages",
      sessionId
    ],

    queryFn: () =>
      getMessages(
        sessionId!
      ),

    enabled: !!sessionId,

    staleTime: 1000 * 30
  });
}
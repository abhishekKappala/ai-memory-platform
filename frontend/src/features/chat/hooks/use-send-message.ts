import {
  useMutation,
  useQueryClient,
} from "@tanstack/react-query";

import {
  sendMessage,
} from "@/services/chat-service";

interface SendMessagePayload {
  sessionId: number;
  content: string;
}

export function useSendMessage() {

  const queryClient =
    useQueryClient();

  return useMutation({

    mutationFn: async ({
      sessionId,
      content,
    }: SendMessagePayload) => {

      return sendMessage(
        sessionId,
        content
      );
    },

    onSuccess: (
      _data,
      variables
    ) => {

      queryClient.invalidateQueries({

        queryKey: [
          "messages",
          variables.sessionId,
        ],

      });
    },

    onError: (
      error
    ) => {

      console.error(
        "Failed to send message:",
        error
      );
    },
  });
}
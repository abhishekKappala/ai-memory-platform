import {

  useQuery

} from "@tanstack/react-query";

import {

  getSessions

} from "@/services/chat-service";

export function useSessions(){

  return useQuery({

    queryKey:["sessions"],

    queryFn:getSessions
  });
}
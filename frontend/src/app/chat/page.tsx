"use client";

import {

  ProtectedRoute

} from "@/components/protected-route";

import {

  ChatLayout

} from "@/features/chat/components/chat-layout";

export default function ChatPage(){

  return(

    <ProtectedRoute>

      <ChatLayout />

    </ProtectedRoute>
  );
}



// "use client";

// import { useRouter } from "next/navigation";

// import {

//   ProtectedRoute

// } from "@/components/protected-route";

// import {

//   useAuthStore

// } from "@/store/auth-store";

// export default function ChatPage() {

//   const router = useRouter();

//   const logout =
//     useAuthStore(
//       (s) => s.logout
//     );

//   function handleLogout() {

//     logout();

//     router.push("/login");
//   }

//   return (

//     <ProtectedRoute>

//       <main

//         className="

//         min-h-screen

//         bg-background

//         text-foreground

//       "

//       >

//         <div

//           className="

//           flex

//           items-center

//           justify-between

//           border-b

//           px-6

//           py-4

//         "

//         >

//           <h1

//             className="

//             text-xl

//             font-semibold

//           "

//           >

//             AI Memory Platform

//           </h1>

//           <button

//             onClick={handleLogout}

//             className="

//             rounded-lg

//             border

//             px-4

//             py-2

//             text-sm

//             hover:bg-muted

//             transition-colors

//             "

//           >

//             Logout

//           </button>

//         </div>

//         <div

//           className="

//           flex

//           items-center

//           justify-center

//           h-[80vh]

//         "

//         >

//           <h2

//             className="

//             text-2xl

//             font-medium

//           "

//           >

//             Chat UI Coming Next

//           </h2>

//         </div>

//       </main>

//     </ProtectedRoute>
//   );
// }
"use client";

import {

  useEffect

} from "react";

import {

  useRouter

} from "next/navigation";

import {

  useAuthStore

} from "@/store/auth-store";

export function ProtectedRoute({

  children,

}: {

  children: React.ReactNode;

}) {

  const router = useRouter();

  const {

    token,

    hydrated,

    loadToken

  } = useAuthStore();

  useEffect(() => {

    loadToken();

  }, []);

  useEffect(() => {

    if (

      hydrated &&

      !token

    ) {

      router.push(
        "/login"
      );
    }

  }, [

    hydrated,

    token
  ]);

  if (!hydrated) {

    return null;
  }

  if (!token) {

    return null;
  }

  return children;
}


// "use client";

// import {

//   useEffect

// } from "react";

// import {

//   useRouter

// } from "next/navigation";

// import {

//   useAuthStore

// } from "@/store/auth-store";


// export function ProtectedRoute({

//   children

// }:{

//   children:
//   React.ReactNode

// }){

//   const token=
//     useAuthStore(
//       s=>s.token
//     );

//   const router=
//     useRouter();

//   useEffect(()=>{

//     if(!token){

//       router.push(
//         "/login"
//       );
//     }

//   },[token]);

//   if(!token){

//     return null;
//   }

//   return children;
// }
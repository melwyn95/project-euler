let m = 10000000000 ;;

(* How to avoid interger overflow while muliplying
   https://www.geeksforgeeks.org/how-to-avoid-overflow-in-modular-multiplication/
*)

let ( * ) = fun a b -> 
  let rec aux a b acc =
    if b = 0 then acc else
    if b mod 2 = 1 then aux ((a * 2) mod m) (b / 2) ((acc + a) mod m)
    else aux ((a * 2) mod m) (b / 2) acc
  in
  (aux (a mod m) b 0) mod m
;;

let fast_pow_mod x n =
  
  let rec pow n =
    if n = 0 then 1 else
    if n mod 2 = 1 then x * (pow (n - 1))
    else let p = pow (n / 2) in p * p
  in
  pow n
;;

let prime = fast_pow_mod 2 7830457 ;;
let prime = prime * 28433 ;;
let prime = prime + 1 ;;

print_endline @@ string_of_int prime ;;
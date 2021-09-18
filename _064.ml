module TupSet = Set.Make(struct
  type t = float * float * float
  let compare (a,b,c) (a',b',c') =
    let s = string_of_float a ^ string_of_float b ^ string_of_float c in
    let s' = string_of_float a' ^ string_of_float b' ^ string_of_float c' in
    compare s s'
end)

(* HACK: :( *)
let round x = floor (x +. 0.1)

let is_square n = n = floor @@ sqrt n *. (floor @@ sqrt n)
    
let next x n d = 
  let y = ((x *. x) -. (d *. d)) /. n in
  let z = floor (n /. (x -. d)) in
  (z, round (z *. y -. d), round y)

let sqrt_period x =
  let i = floor @@ sqrt x in
  let x = sqrt x in
  let (a,b,c) = next x 1.0 i in
  let rec aux (n,d) xs s = 
    let (a,b,c) = next x n d in
    if TupSet.mem (a,b,c) s
    then List.rev xs
    else aux (c,b) ((a,b,c)::xs) (TupSet.add (a,b,c) s)
  in
  let s = TupSet.empty in
  let s = TupSet.add (a,b,c) s in
  aux (c,b) [(a,b,c)] s;;

let period n = List.length @@ sqrt_period n 

let rec range n m =
  if n = m
  then [n]
  else n::(range (n +. 1.0) m) ;;

range 2.0 10000.0
  |> List.filter (fun n -> not (is_square n))
  |> List.map period
  |> List.filter (fun n -> n mod 2 == 1)
  |> List.length
  |> print_int
  |> print_newline ;;
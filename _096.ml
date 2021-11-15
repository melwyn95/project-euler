type cell = 
    Found of int
  | Possible of int list

let puzzle = fun () -> Array.make 81 (Possible [1; 2; 3; 4; 5; 6; 7; 8; 9])

let position x y = 9 * x + y

let reduce x y n p =
  let q = puzzle () in
  for i = 0 to 8 do
    for j = 0 to 8 do
      let idx = position i j in
      if i = x || j = y 
      then (match p.(idx) with
          Found c -> q.(idx) <- p.(idx)
        | Possible xs -> q.(idx) <- Possible (List.filter (fun x -> x != n) xs)
      )
      else q.(idx) <- p.(idx)
    done
  done;
  let x = x / 3 in
  let y = y / 3 in
  for i = 0 to 2 do
    for j = 0 to 2 do
      let idx = position (3* x + i) (3 * y + j) in
      (match q.(idx) with
        Found c -> q.(idx) <- q.(idx)
      | Possible xs -> q.(idx) <- Possible (List.filter (fun x -> x != n) xs))
    done;
  done;
  q
;;

let insert x y n p =
  let idx = position x y in
  if n > 0 then 
    let _ = p.(idx) <- Found n in
    reduce x y n p
  else p
;;

let pp p =
  for i = 0 to 8 do
    for j = 0 to 8 do
      print_string " ";
      (match p.(position i j) with
        Found x -> print_int x;
      | Possible ys -> print_string @@ "X"
      );
      print_string " ";
      if j = 2 || j = 5 then print_string "|";
    done;
    print_newline ();
    if i = 2 || i = 5 
    then print_string "----------------------------\n";
  done;
;;

let input = 
"003020600
900305001
001806400
008102900
700000008
006708200
002609500
800203009
005010300"

let hardest = 
"800000000
003600000
070090200
050007000
000045700
000100030
001000068
008500010
090000400"

let lines = String.split_on_char '\n' ;; 

let zero_ascii = int_of_char '0';;

let parse input =
  let p = ref @@ puzzle () in
  List.iteri (fun i s -> 
    String.iteri (fun j c -> 
        let c = int_of_char c  - zero_ascii in
        if c > 0 
        then !p.(position i j) <- Found c; p := insert i j c !p;
      ) s) input ;
  !p

let p = parse @@ lines hardest ;;

(* pp p ;; *)
  
let is_solved p =
  not @@ Array.exists (function Possible _ -> true | _ -> false) p

let is_solvable p = 
  Array.exists (function Possible xs -> List.length xs > 0 | _ -> false) p

let get_possible = function Possible xs -> xs | _ -> failwith "error: get_possible"

let get_found = function Found c -> c | _ -> failwith "error: get_found"

let rec solve p =
  if is_solved p then Some p
  else if is_solvable p then
    let min_pos = ref (-1, -1, 10) in
    for i = 0 to 8 do
      for j = 0 to 8 do
        let idx = position i j in
        let poss = p.(idx) in
        (match poss with
          Found _ -> ()
        | Possible xs -> 
          let (_, _, len) = !min_pos in
          let len' = List.length xs in 
          if len' < len then min_pos := (i, j, len'); 
        )
      done;
    done;
    let (i, j, len) = !min_pos in
    let idx = position i j in
    let poss = get_possible (p.(idx)) in
    let rec aux poss = 
      match poss with
        [] -> None
      | pos::poss ->
        let s = solve (insert i j pos p) in
        if Option.is_some s then s else aux poss
    in
    aux poss
  else None
;;

let p = solve p ;;

let p = Option.get p ;;

pp p ;;

let read_file_lines filename =
  let ch = open_in filename in
  let s = String.split_on_char '\n' @@ really_input_string ch (in_channel_length ch) in
  close_in ch;
  s;;

let input = read_file_lines "./inputs/_096" ;;
let _,_,input = List.fold_left (fun (i,xs,ys) x -> 
    if i = 10 
    then (1,[],(List.rev (x::xs))::ys) 
    else (i+1,x::xs,ys)
  ) (1,[],[]) input;;

let solution p = p 
  |> List.tl 
  |> parse 
  |> solve 
  |> Option.get 
  |> (fun xs -> xs.(0),xs.(1),xs.(2))
  |> (fun (a,b,c) -> 100 * get_found a + 10 * get_found b + get_found c)
;;
let input = List.map solution input ;;
let input = List.fold_left (+) 0 input ;;

print_int input ;;
print_newline () ;;
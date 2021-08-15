type suit = Heart | Diamond | Club | Spade

type value = Value of int | Jack | King | Queen | Ace

type card = suit * value

type one_pair = [`OnePair of value]
type three_kind = [`ThreeKind of value]

type rank = [
  | `HighCard of value 
  | one_pair
  | `TwoPairs of one_pair * one_pair 
  | three_kind
  | `Straight
  | `Flush
  | `FullHouse of three_kind * one_pair
  | `FourKind of value
  | `StraightFlush
  | `RoyalFlush]

(* let pp_value =
  function
    Value n -> "Value (" ^ string_of_int n ^ ") "
  | Jack -> "Jack"
  | King -> "King"
  | Queen -> "Queen"
  | Ace -> "Ace"

let rec pp_rank (rank : rank) = 
  match rank with
    `HighCard v -> "HighCard (" ^ pp_value v ^ ") "
  | `OnePair v -> "OnePair (" ^ pp_value v ^ ") "
  | `TwoPairs (v1, v2) -> "TwoPairs (" (* ^ pp_rank v1 ^ ", " ^ pp_rank v2 ^ ") "*)
  | `ThreeKind v -> "ThreeKind (" ^ pp_value v ^ ") "
  | `Straight -> "Straight"
  | `Flush -> "Flush"
  | `FullHouse (v1, v2) -> "FullHouse (" (* ^ pp_rank v1 ^ ", " ^ pp_rank v2 ^ ") "*)
  | `FourKind v -> "FourKind (" ^ pp_value v ^ ") "
  | `StraightFlush -> "StraightFlush"
  | `RoyalFlush -> "RoyalFlush" *)
  
let compare_values x y = 
  match (x, y) with
  | (Value x), (Value y) -> if x > y then (Value x) else (Value y)
  | Jack, (Value _ | Jack)
  | (Value _), Jack -> Jack
  | Queen, (Value _ | Jack | Queen)
  | (Value _ | Jack), Queen  -> Queen
  | King, (Value _ | Jack | Queen | King) 
  | (Value _ | Jack | Queen), King -> King
  | Ace, _ | _, Ace -> Ace 

let are_cards_consecutive = 
  function 
  | [(_, Value 2); (_, Value 3); (_, Value 4); (_, Value 5); (_, Value 6)]
  | [(_, Value 3); (_, Value 4); (_, Value 5); (_, Value 6); (_, Value 7)]
  | [(_, Value 4); (_, Value 5); (_, Value 6); (_, Value 7); (_, Value 8)]
  | [(_, Value 5); (_, Value 6); (_, Value 7); (_, Value 8); (_, Value 9)]
  | [(_, Value 6); (_, Value 7); (_, Value 8); (_, Value 9); (_, Value 10)]
  | [(_, Value 7); (_, Value 8); (_, Value 9); (_, Value 10); (_, Jack)]
  | [(_, Value 8); (_, Value 9); (_, Value 10); (_, Jack); (_, Queen)]
  | [(_, Value 9); (_, Value 10); (_, Jack); (_, Queen); (_, King)]
  | [(_, Value 10); (_, Jack); (_, Queen); (_, King); (_, Ace)] -> true
  | _ -> false 
    
let are_cards_same_suit =
  function 
    [(Heart, _); (Heart, _); (Heart, _); (Heart, _); (Heart, _)]
  | [(Diamond, _); (Diamond, _); (Diamond, _); (Diamond, _); (Diamond, _)]
  | [(Club, _); (Club, _); (Club, _); (Club, _); (Club, _)]
  | [(Spade, _); (Spade, _); (Spade, _); (Spade, _); (Spade, _)] -> true
  | _ -> false

let is_royal_flush cards = 
  match cards with 
    [(_, Value 10); (_, Jack); (_, Queen); (_, King); (_, Ace)] -> are_cards_same_suit cards
  | _ -> false

let high_card cards = 
  List.fold_left compare_values (Value 0) @@ List.map snd cards;;

let card_occurances cards = List.fold_left 
    (fun (assoc : (value * int) list) (_, (value : value )) -> 
       if List.mem_assoc value assoc
       then 
         let count = List.assoc value assoc in
         let assoc = List.remove_assoc value assoc in
         (value, count + 1) ::assoc
       else (value, 1) :: assoc
    ) [] cards 
    
let occ_cmp (_, x) (_, y) = 
  Stdlib.compare x y
    
let int_card_value =
  function
    Value n -> n
  | Jack -> 11
  | King -> 12
  | Queen -> 13
  | Ace -> 14
      

let rank_cards cards : rank = 
  if is_royal_flush cards then `RoyalFlush
  else if are_cards_same_suit cards && are_cards_consecutive cards then `StraightFlush
  else if are_cards_same_suit cards then `Flush
  else if are_cards_consecutive cards then `Straight
  else 
    let card_occs = List.sort occ_cmp  @@ card_occurances cards in
    match List.length card_occs with
    | 2 -> 
        (match card_occs with 
         | [(_, 1); (v, 4)] -> `FourKind v
         | [(v1, 2); (v2, 3)] -> `FullHouse (`ThreeKind v2, `OnePair v1)
         | _ -> failwith "card_occs lenght: 2"
        )
    | 3 -> 
        (match card_occs with
         | [(_, 1); (v1, 2); (v2, 2)] -> 
             if int_card_value v1 > int_card_value v2
             then `TwoPairs (`OnePair v1, `OnePair v2)
             else `TwoPairs (`OnePair v2, `OnePair v1)
         | [(_, 1); (_, 1); (v, 3)] -> `ThreeKind v
         | _ -> failwith "card_occs length: 3"
        )
    | 4 ->
        (match card_occs with
         | [_; _; _; (v, 2)] -> `OnePair v 
         | _ -> failwith "card_occs length: 4"
        )
    | 5 -> `HighCard (high_card cards)
    | _ -> failwith "card_occs invalid length";; 
        
let separate xs = 
  let rec aux n xs ys = 
    if n = 0
    then (List.rev xs, ys)
    else 
      match ys with
      | y :: ys -> aux (n - 1) (y :: xs) ys
      | [] -> failwith "separate: empty list"
  in
  aux 5 [] xs
  
let parse_card c =
  let suit = match c.[1] with
    | 'H' -> Heart
    | 'D' -> Diamond
    | 'S' -> Spade
    | 'C' -> Club 
    | _  -> failwith "parse error: invalid suit" in
  let value = match c.[0] with
    | '2' .. '9' -> Value (int_of_char c.[0] - 48)
    | 'T' -> Value 10
    | 'K' -> King
    | 'Q' -> Queen
    | 'J' -> Jack
    | 'A' -> Ace 
    | _ -> failwith "parse error: invalid value"
  in
  (suit, value)
  
let print_list xs =
  List.iter (fun x -> print_int x; print_string " ") xs;
  print_newline ();;

let rec compare_lists xs ys = 
  match (xs, ys) with
  | (x :: xs), (y :: ys) -> if x > y
      then true
      else if x < y
      then false
      else compare_lists xs ys
  | _ -> failwith "invalid: compare_lists"
  
let compare_ranks r1 r2 xs ys = 
  match (r1, r2) with
  | `TwoPairs (`OnePair v1, `OnePair v2), `TwoPairs (`OnePair v3, `OnePair v4)
  | `FullHouse (`ThreeKind v1, `OnePair v2), `FullHouse (`ThreeKind v3, `OnePair v4) ->
    if int_card_value v1 > int_card_value v3
    then true
    else if int_card_value v1 = int_card_value v3
    then 
      if int_card_value v2 > int_card_value v4
      then true
      else if int_card_value v2 = int_card_value v4
      then compare_lists xs ys
      else false
    else false
  | `RoyalFlush, `RoyalFlush 
  | `StraightFlush, `StraightFlush
  | `Flush, `Flush
  | `Straight, `Straight -> 
    compare_lists xs ys
  | `OnePair v1, `OnePair v2
  | `HighCard v1, `HighCard v2
  | `FourKind v1, `FourKind v2
  | `ThreeKind v1, `ThreeKind v2 -> 
    if int_card_value v1 > int_card_value v2
    then true
    else if int_card_value v1 = int_card_value v2
    then compare_lists xs ys
    else false
  
  | _, `RoyalFlush
  | `FourKind _, `StraightFlush
  | `FullHouse _, (`FourKind _ | `StraightFlush) 
  | `Flush, (`FullHouse _ | `FourKind _ | `StraightFlush) 
  | `Straight, (`Flush | `FullHouse _ | `FourKind _ | `StraightFlush) 
  | `ThreeKind _, (`Straight | `Flush | `FullHouse _ | `FourKind _ | `StraightFlush) 
  | `TwoPairs _, (`ThreeKind _ | `Straight | `Flush | `FullHouse _ | `FourKind _ | `StraightFlush) 
  | `OnePair _, (`TwoPairs _ | `ThreeKind _ | `Straight | `Flush | `FullHouse _ | `FourKind _ | `StraightFlush) 
  | `HighCard _, _ -> false

  | `RoyalFlush, _
  | `StraightFlush, _ 
  | `FourKind _, _ 
  | `FullHouse _, _ 
  | `Flush, _
  | `Straight, _ 
  | `ThreeKind _, _
  | `TwoPairs _, _ 
  | `OnePair _, _ -> true
  
let parse_line s = 
  let ss = String.split_on_char ' ' s in
  let cards = List.map parse_card ss in
  let first, second = separate cards in
  let rank_first, rank_second = rank_cards first, rank_cards second in
  let value_first, value_second =
    List.rev @@ List.sort Stdlib.compare @@ List.map int_card_value @@ List.map snd first,
    List.rev @@ List.sort Stdlib.compare @@ List.map int_card_value @@ List.map snd second in
  if compare_ranks rank_first rank_second value_first value_second
  then 1
  else 0;;
    
    
assert (parse_line "5H 5C 6S 7S KD 2C 3S 8S 8D TD" = 0);;
assert (parse_line "5D 8C 9S JS AC 2C 5C 7D 8S QH" = 1);;
assert (parse_line "2D 9C AS AH AC 3D 6D 7D TD QD" = 0);;
assert (parse_line "4D 6S 9H QH QC 3D 6D 7H QD QS" = 1);;
assert (parse_line "2H 2D 4C 4D 4S 3C 3D 3S 9S 9D" = 1);;

let read_file_lines filename =
  let ch = open_in filename in
  let s = String.split_on_char '\n' @@ really_input_string ch (in_channel_length ch) in
  close_in ch;
  s;;

let answer = List.fold_left (fun acc line -> acc + parse_line line) 0 @@ read_file_lines "./inputs/_054" ;;

print_endline (string_of_int answer);


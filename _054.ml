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
  
let compare_values x y = 
  match (x, y) with
  | (Value x), (Value y) -> if x > y then (Value x) else (Value y)
  | Jack, (Value _ | Jack)
  | (Value _), Jack -> Jack
  | King, (Value _ | Jack | King)
  | (Value _ | Jack), King  -> King
  | Queen, (Value _ | Jack | King | Queen) 
  | (Value _ | Jack | King), Queen-> Queen
  | Ace, _ | _, Ace-> Ace 

let are_cards_consecutive = 
  function 
    [(_, Value 1); (_, Value 2); (_, Value 3); (_, Value 4); (_, Value 5)]
  | [(_, Value 2); (_, Value 3); (_, Value 4); (_, Value 5); (_, Value 6)]
  | [(_, Value 3); (_, Value 4); (_, Value 5); (_, Value 6); (_, Value 7)]
  | [(_, Value 4); (_, Value 5); (_, Value 6); (_, Value 7); (_, Value 8)]
  | [(_, Value 5); (_, Value 6); (_, Value 7); (_, Value 8); (_, Value 9)]
  | [(_, Value 6); (_, Value 7); (_, Value 8); (_, Value 9); (_, Value 10)]
  | [(_, Value 7); (_, Value 8); (_, Value 9); (_, Value 10); (_, Jack)]
  | [(_, Value 8); (_, Value 9); (_, Value 10); (_, Jack); (_, King)]
  | [(_, Value 9); (_, Value 10); (_, Jack); (_, King); (_, Queen)]
  | [(_, Value 10); (_, Jack); (_, King); (_, Queen); (_, Ace)] -> true
  | _ -> false 
    
let are_cards_same_suit =
  function 
    [(Heart, _); (Heart, _); (Heart, _); (Heart, _); (Heart, _)]
  | [(Diamond, _); (Diamond, _); (Diamond, _); (Diamond, _); (Diamond, _)]
  | [(Club, _); (Club, _); (Club, _); (Club, _); (Club, _)]
  | [(Spade, _); (Spade, _); (Spade, _); (Spade, _); (Spade, _)] -> true
  | _ -> false

let is_royal_flush = 
  function 
    [(_, Value 10); (_, Jack); (_, King); (_, Queen); (_, Ace)] 
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
  if are_cards_same_suit cards
  then 
    if is_royal_flush cards
    then `RoyalFlush
    else if are_cards_consecutive cards
    then `StraightFlush
    else `Flush
  else if are_cards_consecutive cards
  then `Straight
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
         | [_; (v1, 2); (v2, 2)] -> 
             if int_card_value v1 > int_card_value v2
             then `TwoPairs (`OnePair v1, `OnePair v2)
             else `TwoPairs (`OnePair v2, `OnePair v1)
         | [_; _; (v, 3)] -> `ThreeKind v
         | _ -> failwith "card_occs length: 3"
        )
    | 4 ->
        (match card_occs with
         | [_; _; _; (v, 2)] ->  `OnePair v 
         | _ -> failwith "card_occs length: 4"
        )
    | 1 | 5 -> `HighCard (high_card @@ cards)
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
    | '0' .. '9' -> Value (int_of_char c.[0] - 48)
    | 'T' -> Value 10
    | 'K' -> King
    | 'Q' -> Queen
    | 'J' -> Jack
    | 'A' -> Ace 
    | _ -> failwith "parse error: invalid value"
  in
  (suit, value)
  

let rec compare_lists xs ys = 
  match (xs, ys) with
  | (x :: xs), (y :: ys) -> if x > y
      then true
      else compare_lists xs ys
  | _ -> failwith "invalid: compare_lists"
  
let compare_ranks r1 r2 xs ys = 
  match (r1, r2) with
  | `RoyalFlush, `RoyalFlush -> 
      compare_lists xs ys
  | `RoyalFlush, _ -> true
  | _, `RoyalFlush -> false 
  | `StraightFlush, `StraightFlush ->
      compare_lists xs ys
  | `StraightFlush, _ -> true
  | `FourKind v1, `FourKind v2 ->
      if int_card_value v1 > int_card_value v2
      then true
      else if int_card_value v1 = int_card_value v2
      then compare_lists xs ys
      else false
  | `FourKind _, `StraightFlush -> false
  | `FourKind _, _ -> true
  | `FullHouse (`ThreeKind v1, `OnePair v2), `FullHouse (`ThreeKind v3, `OnePair v4) ->
      if int_card_value v1 > int_card_value v3
      then true
      else if int_card_value v1 = int_card_value v2
      then 
        if int_card_value v2 > int_card_value v4
        then true
        else if int_card_value v2 = int_card_value v4
        then compare_lists xs ys
        else false
      else false
  | `FullHouse _, (`StraightFlush | `FourKind _) -> false
  | `FullHouse _, _ -> true
  | `Flush, `Flush ->
      compare_lists xs ys
  | `Flush, (`StraightFlush | `FourKind _ | `FullHouse _) -> false
  | `Flush, _ -> true
  | `Straight, `Straight ->
      compare_lists xs ys
  | `Straight, 
    (`StraightFlush | `FourKind _ | `FullHouse _ | `Flush) -> false
  | `Straight, _ -> true
  | `ThreeKind v1, `ThreeKind v2 -> 
      if int_card_value v1 > int_card_value v2
      then true
      else if int_card_value v1 = int_card_value v2
      then compare_lists xs ys
      else false
  | `ThreeKind _, 
    (`StraightFlush | `FourKind _ | `FullHouse _ | `Flush | `Straight) -> false
  | `ThreeKind _, _ -> true
  | `TwoPairs (`OnePair v1, `OnePair v2), `TwoPairs (`OnePair v3, `OnePair v4) -> 
      if int_card_value v1 > int_card_value v3
      then true
      else if int_card_value v1 = int_card_value v2
      then 
        if int_card_value v2 > int_card_value v4
        then true
        else if int_card_value v2 = int_card_value v4
        then compare_lists xs ys
        else false
      else false
  | `TwoPairs _, 
    (`StraightFlush | `FourKind _ | `FullHouse _ | `Flush | `Straight | `ThreeKind _) -> false
  | `TwoPairs _, _ -> true
  | `OnePair v1, `OnePair v2 -> 
      if int_card_value v1 > int_card_value v2
      then true
      else if int_card_value v1 = int_card_value v2
      then compare_lists xs ys
      else false
  | `OnePair _, 
    (`StraightFlush | `FourKind _ | `FullHouse _ | `Flush | `Straight | `ThreeKind _ | `TwoPairs _) -> false
  | `OnePair _, _ -> true
  | `HighCard v1, `HighCard v2 -> 
      if int_card_value v1 > int_card_value v2
      then true
      else if int_card_value v1 = int_card_value v2
      then compare_lists xs ys
      else false
  | `HighCard _, _ -> false
  
let parse_line s = 
  let ss = String.split_on_char ' ' s in
  let cards = List.map parse_card ss in
  let first, second = separate cards in
  let rank_first, rank_second = rank_cards first, rank_cards second in
  let value_first, value_second =
    List.map int_card_value @@ List.map snd first,
    List.map int_card_value @@ List.map snd second in
  if compare_ranks rank_first rank_second value_first value_second
  then 1
  else 0;;
    
    
(* parse_line "5H 5C 6S 7S KD 2C 3S 8S 8D TD";;
parse_line "5D 8C 9S JS AC 2C 5C 7D 8S QH";;
parse_line "2D 9C AS AH AC 3D 6D 7D TD QD";;
parse_line "4D 6S 9H QH QC 3D 6D 7H QD QS";;
parse_line "2H 2D 4C 4D 4S 3C 3D 3S 9S 9D";; *)

let read_file_lines filename =
  let ch = open_in filename in
  let s = String.split_on_char '\n' @@ really_input_string ch (in_channel_length ch) in
  close_in ch;
  s;;

let answer = List.fold_left (fun acc line -> acc + parse_line line) 0 @@ read_file_lines "./inputs/_054" ;;

print_endline (string_of_int answer);


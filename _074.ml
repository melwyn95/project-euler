let digit_factorial = function 
    0 -> 1
  | 1 -> 1
  | 2 -> 2
  | 3 -> 6
  | 4 -> 24
  | 5 -> 120
  | 6 -> 720
  | 7 -> 5040
  | 8 -> 40320
  | 9 -> 362880
  | _ -> failwith "invalid digit" ;;

let rec digits_factorial_sum n =
  if n = 0 then 0
  else (digit_factorial (n mod 10)) + (digits_factorial_sum (n / 10)) ;;

module IntSet = Set.Make(Int)
let h = Hashtbl.create 100000

let rec main n s h =
  if Hashtbl.mem h n then Hashtbl.find h n
  else if IntSet.mem n s then 0
  else 1 + (main (digits_factorial_sum n) (IntSet.add n s) h) ;;

let c = ref 0 ;;

for n = 0 to 1000000 do
  let chain = main n IntSet.empty h in
  let _ = Hashtbl.add h n chain in
  if 60 = chain then incr c else ()
done ;;

print_int !c ;;
print_newline () ;;

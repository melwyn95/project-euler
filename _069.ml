let _N = 1000007;;
let numbers = Array.make _N true ;; 
numbers.(0) <- false ;;
numbers.(1) <- false ;;

let rec seive n =
  if n = _N 
  then ()
  else if numbers.(n)
  then begin
    let rec aux m =
      if m * n >= _N then ()
      else begin 
        (numbers.(m * n) <- false);
        aux (m  + 1)
      end
    in
    aux 2;
    seive (n + 1);
  end
  else seive (n + 1) ;;

let rec collect n xs =
  if n = _N then List.rev xs
  else if numbers.(n) then collect (n + 1) (n :: xs)
  else collect (n + 1) xs ;;
  
seive 2;;
let primes = collect 2 [];;

let rec pow x n =
  if n = 1 then x
  else if n = 0 then 1
  else if n mod 2 = 0 
  then let xn = pow x (n / 2) in xn * xn
  else x * pow x (n - 1)

let factorize n =
  let rec foo n p t =
    if n mod p = 0 
    then foo (n / p) p (t + 1)
    else t, n
  in
  let rec aux n ps =
    if numbers.(n)
    then [(n,1)]
    else if n = 1 then []
    else
      match ps with
        [] -> []
      | p :: ps -> 
          if n mod p = 0 
          then 
            let t,n = foo n p 0 in
            (p,t)::aux n ps
          else aux n ps
  in
  let r = aux n primes in
  r ;;


let phi n =
  let factors = factorize n in
  let rec aux fs r = 
    match fs with
      [] -> r
    | (p,n) :: fs -> aux fs (r * (pow p (n - 1)) * (p - 1))
  in
  aux factors 1
;;

let max_n_by_phi = ref (0.0, -1) ;;

for n = 2 to (_N - 7) do
  let p = phi n in
  let np = (float_of_int n) /. (float_of_int p) in
  let mnp, _ = !max_n_by_phi in
  if np > mnp then max_n_by_phi := (np, n) else () 
done

let mnp,max_n = !max_n_by_phi ;;
print_int max_n ;;
print_newline () ;;
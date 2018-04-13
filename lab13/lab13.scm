;; Scheme ;;
(define (reverse l)
  (if (null? l)
     nil
     (append (reverse (cdr l)) (list (car l)))
  )
)

(define (compose-all funcs)
  (define (helper list_funcs x)
          (if (null? list_funcs)
              x
              (helper (cdr list_funcs) ((car list_funcs) x))
          )
  )
  (lambda (input) (helper funcs input))
)

(define (deep-map fn s)
  (if (null? s)
    nil
    (if (list? (car s))
          (cons (deep-map fn (car s)) (deep-map fn (cdr s)))
          (cons (fn (car s)) (deep-map fn (cdr s)))
    )
  )
)

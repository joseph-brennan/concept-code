;;;; Lisp practice code
;; sbcl along with (test '() )
(defun test (lst)
	(cond ((null lst) nil)
	      ((car lst) (cons (car lst) (test (cdr lst))))
	)
) 

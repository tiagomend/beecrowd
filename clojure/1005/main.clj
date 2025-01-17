(defn average-one []
  (let [a (Double/parseDouble (read-line))
        b (Double/parseDouble (read-line))
        weight-of-a 3.5
        weight-of-b 7.5
        media (/ (+ (* a weight-of-a) (* b weight-of-b))
                 (+ weight-of-a weight-of-b))]
    (format "MEDIA = %.5f" media)))

(println (average-one))

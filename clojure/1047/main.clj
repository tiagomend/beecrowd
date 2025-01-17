(defn hours-to-minutes [hours]
  (* hours 60))

(defn minutes-to-hours [minutes]
  (let [hours (quot minutes 60)
        remaining-minutes (rem minutes 60)]
    [hours remaining-minutes]))

(defn split-input []
  (mapv #(Integer/parseInt %) (clojure.string/split (read-line) #"\s+")))

(defn calculate-duration [start end]
  (if (> end start)
    (- end start)
    (+ (- 1440 start) end)))

(defn game-time-in-minutes []
  (let [[start-hour start-minute end-hour end-minute] (split-input)
        start-minutes (+ (hours-to-minutes start-hour) start-minute)
        end-minutes (+ (hours-to-minutes end-hour) end-minute)
        duration-in-minutes (calculate-duration start-minutes end-minutes)
        duration-in-minutes (if (= duration-in-minutes 0) 1440 duration-in-minutes)
        [hours minutes] (minutes-to-hours duration-in-minutes)]
    (str "O JOGO DUROU " hours " HORA(S) E " minutes " MINUTO(S)")))

(println (game-time-in-minutes))

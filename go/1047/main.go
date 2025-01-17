package main

import ("fmt")

func hoursToMinutes(hours int) int {
	return hours * 60
}

func minutesToHours(minutes int) (int, int){
	hours := minutes / 60
	remainingMinutes := minutes % 60
	return hours, remainingMinutes
}

func splitInput()(int, int, int, int){
	var startHour, startMinute, endHour, endMinute int
	fmt.Scan(&startHour, &startMinute, &endHour, &endMinute)
	return startHour, startMinute, endHour, endMinute
}

func calculateDuration(start, end int) int {
	if end > start {
		return end - start
	}
	return 1440 - start + end
}

func gameTimeInMinutes() string {
	startHour, startMinute, endHour, endMinute := splitInput()
	startMinutes := hoursToMinutes(startHour) + startMinute
	endMinutes := hoursToMinutes(endHour) + endMinute

	durationInMinutes := calculateDuration(startMinutes, endMinutes)

	if durationInMinutes == 0 {
		durationInMinutes = 1440
	}

	hours, minutes := minutesToHours(durationInMinutes)
	return fmt.Sprintf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)", hours, minutes)
}

func main(){
	fmt.Println(gameTimeInMinutes())
}
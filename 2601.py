# unc main() {

# coral := [4]string{"blue coral", "foliose coral", "pillar coral", "elkhorn coral"}

# coral = append(coral, "brown coral")

# fmt.Println(coral)

# }


# [15:46] Avinash Upadhya (Nokia)

# func q1() {

# 	var a [5]int = [5]int{0, 1, 2}

# 	b := a[1:4]

# 	fmt.Print(len(b), cap(b), b)

# }

# [15:48] Avinash Upadhya (Nokia)

# func q1() {

# 	var a [5]int = [5]int{0, 1, 2}

# 	b := a[1:4]

# 	add(b)

# 	fmt.Print(len(b), cap(b), b)

# }


# func add(s []int) {

# 	s[1] = 10

# 	s = append(s, 20)

# 	s = append(s, 30)

# 	s[0] = 9

# 	s[2] = 100

# }

func selectionSort<T>(_ inArray: [T], comparator:(T, T)->Int) -> [T] {
    var array = inArray
    
    for i in 0..<(array.count) {
        var smallest = i
        for j in i..<(array.count) {
            if comparator(array[smallest], array[j]) < 0 {
                smallest = j
            }
        }
        let temp = array[i]
        array[i] = array[smallest]
        array[smallest] = temp
    }
    return array
}

print(selectionSort([32,3,43,6,45,56,2,67,32,65]) {
    $1 - $0
})

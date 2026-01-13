#!/usr/bin/env python3
"""Generate a tutorial for the made-up language "Luma"."""

from __future__ import annotations

from pathlib import Path


TUTORIAL = """# Luma Programming Language Tutorial

Luma is a made-up, friendly language with Python-like indentation and Java-style
classes. It uses `fun` for functions, `let` for variables, and `class` for
object-oriented design. Indentation is significant and blocks are ended by
unindenting.

## Hello, Luma!

```luma
fun main():
    print("Hello, Luma!")
```

## Variables and Types

```luma
let name: Text = "Ari"
let age: Int = 21
let pi: Float = 3.1415
let active: Bool = true
```

## Conditionals

```luma
fun grade(score: Int): Text:
    if score >= 90:
        return "A"
    else if score >= 80:
        return "B"
    else:
        return "C"
```

## Loops

```luma
fun countdown(from: Int):
    let i: Int = from
    while i > 0:
        print(i)
        i = i - 1
    print("Lift off!")
```

## Collections

```luma
let numbers: List<Int> = [5, 2, 9, 1]
let mapping: Map<Text, Int> = {"apples": 3, "oranges": 5}
```

## Functions

```luma
fun add(a: Int, b: Int): Int:
    return a + b
```

## Classes

```luma
class Counter:
    let value: Int = 0

    fun increment():
        self.value = self.value + 1

    fun toText(): Text:
        return "Counter(" + self.value + ")"
```

## Algorithms

### Bubble Sort

```luma
fun bubbleSort(items: List<Int>): List<Int>:
    let n: Int = items.length
    let i: Int = 0
    while i < n:
        let j: Int = 0
        while j < n - i - 1:
            if items[j] > items[j + 1]:
                let temp: Int = items[j]
                items[j] = items[j + 1]
                items[j + 1] = temp
            j = j + 1
        i = i + 1
    return items
```

### Insertion Sort

```luma
fun insertionSort(items: List<Int>): List<Int>:
    let i: Int = 1
    while i < items.length:
        let key: Int = items[i]
        let j: Int = i - 1
        while j >= 0 and items[j] > key:
            items[j + 1] = items[j]
            j = j - 1
        items[j + 1] = key
        i = i + 1
    return items
```

### Linear Search

```luma
fun linearSearch(items: List<Int>, target: Int): Int:
    let i: Int = 0
    while i < items.length:
        if items[i] == target:
            return i
        i = i + 1
    return -1
```

### Binary Search

```luma
fun binarySearch(sorted: List<Int>, target: Int): Int:
    let low: Int = 0
    let high: Int = sorted.length - 1

    while low <= high:
        let mid: Int = (low + high) / 2
        if sorted[mid] == target:
            return mid
        else if sorted[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

## Example Program

```luma
fun main():
    let data: List<Int> = [9, 2, 5, 1, 8]
    let sorted: List<Int> = bubbleSort(data)
    print("Sorted: " + sorted)
    let index: Int = binarySearch(sorted, 5)
    print("Index of 5: " + index)
```
"""


def main() -> None:
    output_path = Path("tutorial.md")
    output_path.write_text(TUTORIAL, encoding="utf-8")
    print(f"Wrote tutorial to {output_path}")


if __name__ == "__main__":
    main()

{:ok, input} = File.read "01.txt"

sequence = input
|> String.trim
|> String.split("", trim: true)
|> Enum.map(&String.to_integer/1)

sequence
|> (fn [hd | tl] -> [hd | tl] ++ [hd] end).()
|> Enum.chunk_every(2, 1, :discard)
|> Enum.filter(fn [a, b] -> a == b end)
|> Enum.reduce(0, fn ([n , _], sum) -> sum + n end)
|> IO.inspect

half = div(length(sequence), 2)
first = Enum.slice(sequence, 0, half)
second = Enum.slice(sequence, half, half)

Enum.zip(first, second)
|> Enum.filter(fn {a, b} -> a == b end)
|> Enum.reduce(0, fn ({a, b}, sum) -> sum + a + b end)
|> IO.inspect
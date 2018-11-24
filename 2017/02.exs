{:ok, input} = File.read "02.txt"

# # input = """
# #         5 1 9 5
# #         7 5 3
# #         2 4 6 8
# #         """

rows = String.split(input, "\n", trim: true)

Enum.map(rows, fn row -> 
    String.split(row) 
    |> Enum.map(&String.to_integer/1)
    |> Enum.min_max
    |> (fn {min, max} -> max - min end).() 
    end)
|> Enum.sum
|> IO.inspect

# input = """
# 5 9 2 8
# 9 4 7 3
# 3 8 6 5
# """



Enum.map(rows, fn row -> 
    numbers = String.split(row) |> Enum.map(&String.to_integer/1)
    
    Enum.map(numbers, fn i -> 
        devides? = fn n -> i != n and rem(n, i) == 0 end
        result = Enum.find(numbers, devides?)
        if result do div(result, i) else nil end
    end)
end) 
|> List.flatten
|> Enum.reduce(0, fn(x, acc) -> if x do acc + x else acc end end)
|> IO.inspect

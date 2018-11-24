{:ok, input} = File.read "03.txt"

number = String.to_integer(String.trim(input))

# number = 1024

ring = fn n -> Float.ceil((Float.floor(:math.sqrt(n))) / 2) end


centers = fn ring ->
    square = :math.pow(ring*2+1, 2)
    offset = ring
    jump = 2 * ring
    for n <- 1..4, do: square + offset - (n*jump) end

r = ring.(number)
c = centers.(r)

min = Enum.map(c, fn x -> abs(number - x) end )
|> Enum.min

steps = min + r

IO.puts "#{steps} ring => #{inspect r} centers => #{inspect c}"





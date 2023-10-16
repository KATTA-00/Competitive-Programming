def min_transcription_factors(expression_levels):
    n = len(expression_levels)
    transcription_factors = [1] * n

    for i in range(1, n):
        if expression_levels[i] > expression_levels[i - 1]:
            transcription_factors[i] = transcription_factors[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if expression_levels[i] > expression_levels[i + 1]:
            transcription_factors[i] = max(transcription_factors[i], transcription_factors[i + 1] + 1)

    return sum(transcription_factors)

input_values = input().strip().split()
expression_levels = [int(value) for value in input_values]

result = min_transcription_factors(expression_levels)
print(result)

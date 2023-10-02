# Hash_table
A estrutura escolhida foi o hash table que permite fazer a inserção, remoção e busca numa média de tempo de O(1). Como tem um tempo constante é mais eficiente do que se implementa-se uma arvore AVL que teria complexidade de O(log n).

Inserção: Complexidade de Tempo: Média: O(1). Na pior das hipóteses pode se tornar O(n). Complexidade de Espaço: O(1)

Remoção: Complexidade de Tempo: Média: O(1). Complexidade de Espaço: O(1)

Busca: Complexidade de Tempo: Média é O(1). Complexidade de Espaço: O(1), pois não envolve aumento permanente no uso de memória.

União: Complexidade de Tempo: O(len(s1) + len(s2)) onde s1 e s2 são dois conjuntos. Complexidade de Espaço: O(len(s1) + len(s2))

Interseção: Complexidade de Tempo: O(min(len(s1), len(s2))) onde s1 e s2 são dois conjuntos. Complexidade de Espaço: O(min(len(s1), len(s2)))

Diferença: Complexidade de Tempo: O(len(s1)), onde s1 é o tamanho do conjunto do qual você está subtraindo elementos. Complexidade de Espaço: O(len(s1))

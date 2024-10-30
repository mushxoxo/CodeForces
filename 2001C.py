import sys
def solve_tree(n):
    edges = []

    for i in range(2, n+1):
        response = query(1, i)
        if response == 1:
            edges.append((1, i))
        else:
            edges.append((response, i))
    
    output_tree(edges)

def query(a, b):
    print(f"? {a} {b}")
    sys.stdout.flush()
    return int(input().strip())

def output_tree(edges):
    print("!", " ".join(f"{a} {b}" for a, b in edges))
    sys.stdout.flush()

def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        solve_tree(n)

if __name__ == "__main__":
    main()
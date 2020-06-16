import math

approx_pi = math.pi

def findLambda(N):
    theta_up = approx_pi / (N + 1)
    theta_bot = approx_pi / N
    slope_up = 1 / math.tan(theta_up)
    slope_bot = 1 / math.tan(theta_bot)
    lambda_up = math.pow(slope_up, 2)
    lambda_bot = math.pow(slope_bot, 2)
    print(f"{round(lambda_bot, 2)}, {round(lambda_up, 2)}")


def main():
    N = int(input())
    findLambda(N)

if __name__ == "__main__":
    main()

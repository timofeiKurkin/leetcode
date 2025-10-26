class Bank {
    accounts: number[]
    n: number

    constructor(balance: number[]) {
        this.accounts = balance
        this.n = balance.length
    }

    transfer(account1: number, account2: number, money: number): boolean {
        if (account1 > this.n || account2 > this.n || this.accounts[account1 - 1] < money) {
            return false
        }

        this.accounts[account2 - 1] += money
        this.accounts[account1 - 1] -= money

        return true
    }

    deposit(account: number, money: number): boolean {
        if (account > this.n) {
            return false
        }

        this.accounts[account - 1] += money
        return true
    }

    withdraw(account: number, money: number): boolean {
        if (account > this.n || this.accounts[account - 1] < money) {
            return false
        }

        this.accounts[account - 1] -= money
        return true
    }
}

/**
 * Your Bank object will be instantiated and called as such:
 * var obj = new Bank(balance)
 * var param_1 = obj.transfer(account1,account2,money)
 * var param_2 = obj.deposit(account,money)
 * var param_3 = obj.withdraw(account,money)
 */
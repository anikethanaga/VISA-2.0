package com.visa.ATM;

public class Response {

    double amount;
    String name;
    double rate;
    boolean status;

    public void setAmount(double amount) {
        this.amount = amount;
    }

    public void setRate(double rate) {
        this.rate = rate;
    }

    public void setStatus(boolean status) {
        this.status = status;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getAmount() {
        return amount;
    }

    public String getName() {
        return name;
    }

    public double getRate() {
        return rate;
    }

    public boolean isStatus() {
        return status;
    }


}

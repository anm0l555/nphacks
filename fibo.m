clc
clear all

f=@(x) x.*(x-2);
L=0;
R=1.5;
n=6;
t=linspace(L,R,100);
plot(t,f(t))
fib=ones(1,n);

for i=3:n+1
    fib(i)=fib(i-1)+fib(i-2);
end

for k=1:n
    ratio=fib(n-k+1)/fib(n+2-k);
    x2=L+ratio.*(R-L);
    x1=L+R-x2;
    fx1=f(x1);
    fx2=f(x2);
    rs1(k,:)=[L R x1 x2 fx1 fx2];
    if fx1<fx2
        R=x2;
    elseif fx1>fx2
        L=x1;
    elseif fx1==fx2
        if min(abs(x1),abs(L))==abs(L)
            R=x2;
        else
            L=x1;
        end
    end
end

rs1(k,:)=[L R x1 x2 fx1 fx2];
variables={'L','R','x1','x2','fx1','fx2'};
Resf=array2table(rs1);
Resf.Properties.VariableNames(1:size(Resf,2))=variables
Xopt=(L+R)/2
fopt=f(Xopt)
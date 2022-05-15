clc;
clear;
format rat;
M=-10000;
a=[2,4,1,1,0,0;3,5,4,0,-1,1];
b=[8;15];
c=[2,3.5,3.5,0,0,M,0];% extra 0 at end for storing Z
A=[a b];
bv=[4 6];
z_c=c(bv)*A-c;
opttable=[A;z_c];
array2table([A;z_c],'VariableNames',{'x1','x2','x3','s1','s2','a1','sol'},'RowNames',{'s1','a1','z-c1'})
RUN=true;
while RUN
    if any(opttable(end,1:end-1)<0)
        disp('Not optimal ')
        [picol,pivindi]=min(opttable(end,1:end-1))
        if all(opttable(1:end-1,pivindi)<0)
            disp('Unbounded solution')
            break
        end
        for i=1:size(opttable,1)-1
            if opttable(i,pivindi)<0
                ratio(i)=inf;
            else
                ratio(i)=opttable(i,end)/opttable(i,pivindi);
            end
        end
        [min_r,min_rindi]=min(ratio) %pivot row
        pivele=opttable(min_rindi,pivindi)
        bv(min_rindi)=pivindi;
        opttable(min_rindi,:)=opttable(min_rindi,:)/pivele;
        for i=1:size(opttable,1)
            if i~=min_rindi
                opttable(i,:)=opttable(i,:)-opttable(i,pivindi)*opttable(min_rindi,:);
            end
        end
        array2table(opttable,'VariableNames',{'x1','x2','x3','s1','s2','a1','sol'})


    else
        disp('Optimal solution acheived')
        RUN=false;
    end
end
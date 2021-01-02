var
	n:Smallint;
begin
    read(n);
    if n=0 then begin
        write(0)
    end
    else if n<=1000 then begin
        write(1000-n)
    end
    else if n<=2000 then begin
        write(2000-n)
    end
    else if n<=3000 then begin
        write(3000-n)
    end
    else if n<=4000 then begin
        write(4000-n)
    end
    else if n<=5000 then begin
        write(5000-n)
    end
    else if n<=6000 then begin
        write(6000-n)
    end
    else if n<=7000 then begin
        write(7000-n)
    end
    else if n<=8000 then begin
        write(8000-n)
    end
    else if n<=9000 then begin
        write(9000-n)
    end
    else begin
        write(10000-n)
    end;
end.
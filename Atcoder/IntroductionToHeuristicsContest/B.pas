var
    d,ans,i,j:Smallint;
    c,la:Array[1..26] of Smallint;
    s:Array[1..365,1..26] of Smallint;
    t:Array[1..365] of Smallint;
begin
    read(d);
    for i:= 1 to 26 do begin
        read(c[i]);
        la[i]:=0;
    end;
    for i:= 1 to d do begin
        for j:= 1 to 26 do begin
            read(s[i][j]);
        end;
    end;
    for i:= 1 to d do read(t[i]);
    ans:=0;

    for i:= 1 to d do begin
        ans:=ans+s[i,t[i]];
        la[t[i]]:=i;
        for j:= 1 to 26 do begin
            ans:=ans-c[j]*(i-la[j]);
        end;
        writeln(ans);
    end;
end.
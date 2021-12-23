create table if not exists apartment (
    apartment_id serial primary key,
    city varchar(64),
    street varchar(64),
    house_num int,
    floor_num int,
    room_amt int,
    square_amt int,
    cost int
);

insert into apartment 
    (city, street, house_num, floor_num, room_amt, square_amt, cost)
values
    ('samara', 'lenina', 5, 4, 3, 80, 218489),
    ('moscow', 'gagarina', 6, 5, 4, 90, 1782472),
    ('nikolaev', 'gavela', 23, 7, 3, 56, 184904),
    ('vinniza', 'mira', 5, 5, 1, 23, 182933);
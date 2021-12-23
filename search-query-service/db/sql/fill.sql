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
    ('zp', 'lenina', 5, 4, 3, 80, 218489),
    ('dp', 'letova', 6, 5, 4, 90, 1782472),
    ('kiev', 'kurenivska', 23, 7, 3, 56, 184904),
    ('kiev', 'sklyarenko', 5, 5, 1, 23, 182933);
resource "aws_route_table" "public_rtb" {
  vpc_id = aws_vpc.o_and_t.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.o_and_t_gw.id
  }

  tags = {
    Name = "public_rtb"
  }
}

# Association
resource "aws_route_table_association" "a" {
  subnet_id      = aws_subnet.public_subnet1.id
  route_table_id = aws_route_table.public_rtb.id
}

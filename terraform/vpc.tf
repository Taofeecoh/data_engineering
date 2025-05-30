resource "aws_vpc" "o_and_t" {
  cidr_block = "10.20.0.0/16"
  enable_dns_hostnames = true

  tags = {
    Name        = "o_and_t"
    Environment = "development"
    Team        = "tao_and_obinna"
  }
}

# Internet gateway
resource "aws_internet_gateway" "o_and_t_gw" {
  vpc_id = aws_vpc.o_and_t.id

  tags = {
    Name = "o_and_t_gw"
  }
}
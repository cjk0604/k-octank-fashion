## Production Link
 k-octank.shop/

# EC2 Launch Template
## user data
```
#!/bin/bash 
sudo yum update -y
sudo yum install git -y
sudo yum install -y python3
git clone https://github.com/cjk0604/k-octank-fashion.git
cd k-octank-fashion
sudo pip3 install -r requirements.txt
export DATABASE_HOST=
export DATABASE_USER=
export DATABASE_PASSWORD=
export DATABASE_DB_NAME=
python3 app.py
```

# 부하 테스트
## apache benchmark
```
ab -c 300 -n 500 -t 300 http://k-octank.shop/
ab -c 300 -n 500 -t 300 http://k-octank.shop/products/fashion/
```

# Latency
## Cloudfront 거치지 않고 요청
```
curl -s -w '\nLookup Time:\t%{time_namelookup}\nConnect time:\t%{time_connect}\nPreXfer time:\t%{time_pretransfer}\nStartXfer time:\t%{time_starttransfer}\n\nTotal time:\t%{time_total}\n' -o /dev/null http://k-octank-vpc-alb-2-1616693628.us-east-1.elb.amazonaws.com/products/fashion?page=1/
```
- ALB 엔드포인트 (DNS)

## Cloudfront를 통한 요청
```
curl -s -w '\nLookup Time:\t%{time_namelookup}\nConnect time:\t%{time_connect}\nPreXfer time:\t%{time_pretransfer}\nStartXfer time:\t%{time_starttransfer}\n\nTotal time:\t%{time_total}\n' -o /dev/null http://k-octank.shop/products/fashion?page=1/

curl -s -w '\nTotal Time:\t%{time_total}\n' -o /dev/null http://k-octank.shop/ 

```
- dynamic  동적 호스팅

# Bastion Host 연결
## Bastion 호스틑에서 Private Subnet EC2 연결 방법
1. Bastion 호스트를 연결
```
ssh -i "koctank.pem" -N -L 33322:10.10.11.57:22 ec2-user@3.81.174.50 
```

2. 새로운 터미널을 열고 밑에 코드 복사
```
ssh -i koctank.pem -p 33322 ec2-user@localhost 
```

참고: https://boomkim.github.io/2019/12/20/bastion-host-port-forwarding/

# 로그 분석 및 시각화
## Athena에서 CloudFront_access log S3 연결
```
Create database octank
```

table 만들기
```
CREATE EXTERNAL TABLE IF NOT EXISTS octank.cloudfront_logs (
  `date` DATE,
  time STRING,
  location STRING,
  bytes BIGINT,
  request_ip STRING,
  method STRING,
  host STRING,
  uri STRING,
  status INT,
  referrer STRING,
  user_agent STRING,
  query_string STRING,
  cookie STRING,
  result_type STRING,
  request_id STRING,
  host_header STRING,
  request_protocol STRING,
  request_bytes BIGINT,
  time_taken FLOAT,
  xforwarded_for STRING,
  ssl_protocol STRING,
  ssl_cipher STRING,
  response_result_type STRING,
  http_version STRING,
  fle_status STRING,
  fle_encrypted_fields INT,
  c_port INT,
  time_to_first_byte FLOAT,
  x_edge_detailed_result_type STRING,
  sc_content_type STRING,
  sc_content_len BIGINT,
  sc_range_start BIGINT,
  sc_range_end BIGINT
)
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY '\t'
LOCATION 's3://octank-cloudfront-standard-log/'
TBLPROPERTIES ( 'skip.header.line.count'='2' )
```

# Test Query
```
SELECT DISTINCT * 
FROM cloudfront_logs 
LIMIT 10;
```

## Quicksight 연결 및 대시보드 생성
# 인기 페이지 대시보그 생성


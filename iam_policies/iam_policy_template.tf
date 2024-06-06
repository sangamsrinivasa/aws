data "aws_iam_policy_document" "hello" {
  statement {
    sid       = ""
    effect    = "Allow"
    resources = ["*"]

    actions = [
      "ec2:DescribeInstances",
      "ec2:AttachVolumes",
      "ec2:DetachVolumes",
      "ec2:DescribeSnapshots",
      "ec2:DescribeSecurityGroups",
      "ec2:CreateTags",
      "ec2:ReplaceRouteAssociation",
    ]
  }

  statement {
    sid       = ""
    effect    = "Allow"
    resources = ["*"]

    actions = [
      "s3:GetObject",
      "s3:ListObject",
      "s3:CreateTags",
      "s3:PutObject",
      "s3:GetObject",
      "s3:GetObjectVersions",
      "s3:GetBucketLocation",
      "s3:DeleteBucketPolicy",
    ]
  }

  statement {
    sid       = ""
    effect    = "Allow"
    resources = ["*"]

    actions = [
      "ec2:DescribeVPCS",
      "ec2:DescribeSubnets",
      "ec2:DescribeSecurityGroups",
      "ec2:CreateVPC",
      "ec2:DeleteRouteTable",
    ]
  }

  statement {
    sid       = ""
    effect    = "Allow"
    resources = ["*"]
  }

  statement {
    sid       = ""
    effect    = "Allow"
    resources = ["*"]
  }

  statement {
    sid       = ""
    effect    = "Allow"
    resources = ["*"]
  }

  statement {
    sid       = ""
    effect    = "Allow"
    resources = ["*"]
  }
}

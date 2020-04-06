#!/usr/bin/env bash

# Reject pushes that contain commits with messages that do not adhere
# to the defined regex.

# This can be a useful pre-receive hook [1] if you want to ensure every
# commit is associated with a ticket ID.
#
# As an example this hook ensures that the commit message contains a
# JIRA issue formatted as [JIRA-<issue number>].
#
# [1] https://help.github.com/en/enterprise/user/articles/working-with-pre-receive-hooks
#

set -e
zero_commit='0000000000000000000000000000000000000000'
msg_regex='^[A-Za-z0-9][A-Za-z0-9]{0,10}?-[0-9]+'
while read -r oldrev newrev refname; do

	# Branch or tag got deleted, ignore the push
	[ "$newrev" = "$zero_commit" ] && continue
	# Calculate range for new branch/updated branch
	[ "$oldrev" = "$zero_commit" ] && range="$newrev" || range="$oldrev..$newrev"

    printf "oldrev: - %-8s\n" "$oldrev "
    printf "newrev-my: - %-8s\n" "$newrev "
    printf "refname-my: - %-8s\n" "$refname "



	EXIT_CODE=1

	
done

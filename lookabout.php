<?php

function approved(string $dirty){
    $reggie = "/^(?!jx-)[a-z0-9-]+$/";
    $success = preg_match($reggie, $dirty);

    echo "\n";

	if($success){
		echo $dirty." is good\n";
		return;
	}
	echo ' nah ';
	return;
}

approved($argv[1]);

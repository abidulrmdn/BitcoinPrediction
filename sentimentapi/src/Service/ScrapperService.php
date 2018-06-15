<?php
namespace App\Service;

class ScrapperService
{
    private $scrapperEndpoint = 'http://scrapperEndpointIP/twitter/';

    private $hashTag;

    public function __construct($hashTag, $endpoint = null)
    {
        if (null !== $endpoint) {
            $this->scrapperEndpoint = $endpoint . $hashTag;
        }

        $this->hashTag = $hashTag;
    }

    public function execute($postRequest = false)
    {
        $curl = curl_init();
        // Set some options - we are passing in a useragent too here
        curl_setopt_array($curl, array(
            CURLOPT_RETURNTRANSFER => 1,
            CURLOPT_POST => $postRequest ? 1 : 0,
            CURLOPT_URL => $this->scrapperEndpoint . $this->hashTag,
        ));

        $jsonResponse = curl_exec($curl);
        curl_close($curl);

        return $jsonResponse;
    }
}

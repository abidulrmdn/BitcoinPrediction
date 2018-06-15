<?php

namespace App\Controller;

use App\Service\ScrapperService;

class PredictionController
{
    public function index($request, $response, $params)
    {
        $hashtag = $params['hashtag'];

        // scrap real-time data
        $service = new ScrapperService($hashtag);
        $service->execute(true);

        // get the old and new data
        $service = new ScrapperService($hashtag);
        $scrapperResponseJson = $service->execute();

        $scrapperResponse = json_decode($scrapperResponseJson, true);

        // search the hashtag from scrapper database or just send to scrapper service for real-time search
        if (empty($scrapperResponse)) {
            return json_encode([
                'errors' => [
                    'status' => '204',
                    'title' => 'No content',
                    'description' => 'scrapper is returning empty result'
                ]
            ]);
        }

        // write Json to csv
        $date = new \DateTime();
        $filename = sprintf("%s%s%s", $hashtag, $date->getTimestamp(), '.csv');

        $fp = fopen($filename, 'w');
        foreach($scrapperResponse as $row) {
            $newRow = array();
            $timeStamp = new \DateTime($row['timestamp']);
            $newRow[] = $timeStamp->format('Y-m-d');
            $newRow[] = $row['text'];
            fputcsv($fp, $newRow);
        }
        fclose($fp);

        // trigger ML python script
        $command = escapeshellcmd("python3 predict.py $filename");
        $mLResponse = shell_exec($command);
        $mLResponse = trim($mLResponse);
//        var_dump(empty($mLResponse),$mLResponse, "python3 predict.py $filename");exit;

        if ('' === $mLResponse) {
            return json_encode([
                'errors' => [
                    'status' => '204',
                    'title' => 'No content',
                    'description' => 'Sentiment machine learning is returning empty result'
                ]
            ]);
        }

        // send the results to ML service
        $data = ['data' => $mLResponse, 'message' => 'ML prediction result'];
        return json_encode($data);
    }
}

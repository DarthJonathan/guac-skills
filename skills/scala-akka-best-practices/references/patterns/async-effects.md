# Future and DBIO composition, timeouts, and concurrency

390 source-specific cases. Statements retain their historical scope and source stance. Read related PR cases for corrections or alternatives.

## Cases

- A1-0046 — Failure notification and upcoming-date update share investment-cancellation condition
- A1-0047 — Chain recurring-investment futures
- A1-0110 — Avoid another remote instrument-service fetch in PlanTopicSubscriber
- A1-0132 — Use Future.failed in SG compliance checker and fix HK too
- A1-0136 — Resolve AAA through queryLatestDailyMarketValueByPlanId or getLivePlanInstrumentBalances
- A1-0156 — Validate corporate rules before fetching existing profile
- A1-0177 — Sort and createPage in one Future.map and companion Ordering for transaction rows
- A1-0193 — Assign future to val to start parallel with orderRowsFut
- A1-0241 — SG rebalance advisory request fetches unnecessary extra data
- A1-0261 — Instrument upsert uses Future.failed
- A1-0286 — TransactionsDataGenerator owns two-phase ordering and accepts concrete List
- A1-0303 — Fetch only validInstruments in both regions
- A1-0341 — Log access failures with outer recoverWith for all user roles
- A1-0359 — Use Akka Source destinationProfileIds mapAsync with concurrency 2 or 4
- A1-0365 — Do not fetch retail separately
- A1-0383 — Fetch only new exclusive IDs if both validations apply only there
- A1-0384 — Use instrumentCache getLatestInstruments to bypass cache without duplicating grouping
- A1-0398 — Reuse allNewInstruments or move exclusiveAdditions validation up front
- A1-0403 — Compute reusable value once after fetching source, outside destination loop
- A1-0413 — Use rule service from getAllWhitelistedInstruments for RF summaries
- A1-0418 — Move instrument-fetching logic down to fetch once
- A1-0423 — Consider withRetry on FX lookup
- A1-0431 — Retry until investmentTransferId resolves in trading
- A1-0447 — Future reset commands need completion logging and failure handling
- A1-0497 — Log benchmark-fetch failure after retry and continue fund onboarding
- A1-0528 — Fetch MStar basic info with mapAsync(2), id tuple, Sink.seq and toMap
- A1-0544 — Use getAdvisedPortfolioSummary directly
- A1-0554 — Pass fetched InstrumentInfoDto instead of refetching
- A1-0564 — Fetch goals with includePlans false or directly use goalJdbcRepo
- A1-0567 — Use event.goal instead of refetching entire goal
- A1-0585 — Avoid advisory-projection-simulation remote chain for simple compounding
- A1-0603 — Use recover with Seq.empty without wrapping Future
- A1-0606 — Retry needs deferred rather than eager evaluation
- A1-0620 — Retry only inner safeUploadMonthlyChanges without refetching instrument
- A1-0621 — Recover only safeUploadMonthlyChanges rather than full method
- A1-0625 — Private upload fallback retries without stitching then recovers typed and unexpected failures
- A1-0626 — Retry only incomplete error with stitch true and force false
- A1-0640 — MStar no-doc behavior differs by MStar ID and ISIN
- A1-0641 — Trust returned MStar doc per type/locale; retain existing only absent group
- A1-0674 — Return empty only for legitimate no dividends; exhausted fallback throws 5xx
- A1-0676 — Use transform when no second Future call
- A1-0715 — Fetch standalone flag parallel with planMetrics since nonthrowing
- A1-0717 — Futures still sequential until assigned outside comprehension
- A1-0724 — Trigger monthly-data refresh only on changed stitch config
- A1-0797 — Fold optional goalId into successful planId list or filtered plan IDs
- A1-0803 — Run SIP check after advisoryClassification close to actual accept command
- A1-0807 — Wealth-admin retries impossible B2C and missing tenantId group lookups
- A1-0818 — Background SFTP metadata check returns successful Done without for-comprehension
- A1-0821 — Use stream log or wireTap if losing some logs acceptable
- A1-0838 — Do not wrap synchronous Explore result in Future unnecessarily
- A1-0854 — Use Future.failed for standalone validation
- A1-0872 — Return instruments and weights from PortfolioSummary and BasePlanUpsertSummary
- A1-0916 — Start independent goal-approval summary futures as vals then compose
- A1-0929 — Compiler warnings found communication Future map versus flatMap bugs
- A1-0943 — Compiler warning finds map/flatMap bug mixing DBIO and Future
- A1-0960 — Check sgAckCheckConfig before tenant lookup
- A1-0961 — Return hasSipInstruments future directly without yield
- A1-0971 — Fetch only after conditions match in all three flows
- A1-0978 — Get needed planIds from PlanDto without investment/trading fetch
- A1-0988 — Use Sink.ignore
- A1-0989 — Use flatMap for SIP state-change future
- A1-1035 — Validate request before loading existing acknowledgement entity
- A1-1037 — IGT buy leg investOnce may rerun compliance without needed acknowledgements
- A1-1047 — Stream DB once and loop locales inside; otherwise mapAsync(1)
- A1-1048 — Log individual recon invalid records and runFold count
- A1-1053 — Stream templates before locales and validate tags without collecting
- A1-1057 — Normal-query reconciliation concurrency can be 2 or 4
- A1-1058 — Increase parallelism for another normal query
- A1-1064 — Validate tags per template and locale without collecting or exact deduplicated counts
- A1-1065 — Template parallelism 2 and locale 1 with current single locale
- A1-1086 — Start readside and RRT in parallel; timeout RRT via firstCompletedOf
- A1-1087 — Expected ask timeout is not error for RRT use case
- A1-1092 — Always return at least readSideResults; only RRT should time out
- A1-1114 — Start timeout future first; race it against RRT plus merge then warn and refresh readside
- A1-1126 — No readSideFut val needed if fetched first
- A1-1136 — Use parallelism one for commands to same entity
- A1-1145 — Reuse fetched source goals for customer entrypoint and key names by goalId
- A1-1160 — Throw inside map binding or use flatMap binding with Future.failed
- A1-1165 — Chain stream without materializing all acknowledgement inputs
- A1-1185 — findGoal sufficient for SIP warnings
- A1-1187 — Fetch plan details after confirming missing acknowledgements
- A1-1233 — Remove redundant map to Done
- A1-1271 — Check SIP instruments before calling compliance
- A1-1295 — Consider internal repartitioned Kafka topic rather than sequential DB locking
- A1-1296 — Underlying failure releases lock and caller retry rejoins acquisition
- A1-1297 — Force revoke uses deleteRequest matching stale lock
- A1-1301 — MarketDataLock owns acquire retry separately from underlying releaseRetrySettings
- A1-1302 — Normal release must match original lock request
- A1-1314 — Retry RPC task operation before giving up
- A1-1316 — Use Future.unit
- A1-1317 — foreach starts background task cancellations without waiting; confirm intent
- A1-1331 — Use Source for bounded futures rather than start all at once
- A1-1339 — Use Future.unit in second RPC method
- A1-1341 — Prepare manual retrigger endpoints because recovered failures bypass projection retries
- A1-1362 — Use new redemption endpoint even with multiple calls per goal
- A1-1364 — New endpoint already contains flag; extra getRedemptionPlanRedeemableStatusList unnecessary
- A1-1372 — Use getPlanRedeemableValue data instead of extra call; enrich if fields missing
- A1-1413 — mapFut already handles None as Future.successful(None)
- A1-1422 — Bind newRecurring.resolvedFundingInstructions with equals not flatMap
- A1-1427 — Warn and rethrow trade-cancel command so projection retries
- A1-1449 — Decide throw versus retry-and-give-up to avoid projection block
- A1-1450 — Charge service throws so trading projection retries
- A1-1457 — Remove unnecessary fee-resolution recover
- A1-1460 — Remove no-op recover
- A1-1479 — No Future needed for multi-funding expression
- A1-1480 — runFold merge incrementally rather than collect all
- A1-1486 — Use runFold instead of async fold forcing successful Future
- A1-1506 — Use getPortfolio(plan) when no productPortfolio needed
- A1-1563 — Throw rather than Option because buildPortfolioOfferings already handles skip
- A1-1626 — Bound workflow task futures with Akka stream
- A1-1634 — Workflow task search parallelism2 sufficient
- A1-1668 — Use earliestStartYM as endDate to avoid refetching recent data
- A1-1672 — Pass start/end dates to limit stitch fetch response
- A1-1679 — Use Akka stream to avoid starting all stitching Futures
- A1-1700 — Set MStar enddate with startdate to fetch exactly one daily record
- A1-1701 — Background reconciliation makes test flaky if return precedes completion
- A1-1727 — Cache instrument names even for no-longer-TAA instruments
- A1-1730 — Test throws NotFound synchronously instead of Future.failed
- A1-1735 — Approach accepted if no extra lookup
- A1-1817 — Delete charge rows in bounded batches within one stream
- A1-1834 — Map redemption plan and throw instead of flatMap Future.unit
- A1-1842 — Use flatMap
- A1-1869 — Latest-date query or DB join/stream instead of per-row lookup
- A1-1875 — InstrumentCache already batches; remove outer batching
- A1-1877 — Return portfolio then build DTO outside; reuse validated instruments
- A1-1878 — streamAll directly from DB instead of memory-loaded stream
- A1-1880 — Approach still waits Future
- A1-1891 — Entity requests concurrency2 or4 rather than10
- A1-1903 — Prefer MStarId docs and fallback ISIN only on failure/empty
- A1-1941 — succeed returns before inner future and leaks mock invocation into next test
- A1-1957 — Instrument cache already retries
- A1-1964 — RestartSource.onFailuresWithBackoff does not emit failure
- A1-1965 — RestartSource completion means graceful stop, failure unexpected termination
- A1-1970 — Fetch approval task before portfolio creation
- A1-1988 — Do query users need includePlans
- A1-2003 — Feed DB stream directly to Source
- A1-2022 — Recover per instrument so one failed download does not stop next
- A1-2052 — Do not refetch customer-level data for every goal
- A1-2065 — Check isFullRedemption before portfolio lookup for mandatory rebate
- A1-2085 — Skip allowedInstrumentsResponse when stopping recurring schedule
- A1-2095 — Retry interplan simulation request
- A1-2122 — Bound RF fee lookup via Akka stream instead of Future.traverse
- A1-2126 — Fetch RF by distinct tradingAccountTypes rather than per DIY plan
- A1-2173 — Old filter and customer lookup may now unnecessary
- A1-2182 — recover sufficient without further fetch
- A1-2215 — Use readside getInstrumentV2ByIds for email name
- A1-2244 — Chain email and platform-notification futures
- A1-2246 — No grouping needed; mapAsync directly
- A1-2251 — Run MStar docs sync in background
- A1-2252 — Reject AI-only doc for nonactive AI/PI; check instrument flag before customer fetch
- A1-2262 — Start document sync then return successful Done for background handler
- A1-2265 — No instrument fetch needed here
- A1-2266 — Start stream chunk size200KB–500KB to reduce network trips
- A1-2279 — Error-log instead of throw to avoid workflow retries
- A1-2331 — Recover centrally so transform returns T rather than Option[T]
- A1-2333 — Translation failures transient and retryable; recover policy inconsistent
- A1-2334 — Central fetchAndTransform catches logs and returns None
- A1-2347 — Increase rebate processing parallelism to avoid slowness
- A1-2349 — Try parallelism4; node4/8 CPU count uncertain
- A1-2352 — Instrument-cache grouping parallelism2
- A1-2365 — Only project nonempty goal when requested; filter empty monthlyResults
- A1-2377 — Readside getInstrumentV2ByIds sufficient instead of entity
- A2-0070 — Review: Can I propose we move the logic around a little:
- A2-0081 — CreateFixedMaturityProductGoal: If small number of goals then it’s ok, but ideally we could use an async loading cache here \+ go to readside instead of entity
- A2-0153 — InvestmentPlanEventProcessor: Log that we are ignoring this event, and return Future.successful\(Done\) instead
- A2-0272 — SgCustomerDailyFeesCalculator: For potential extension, we can add `allowedPlanFeeInstructionOverride` to `PlanChargeContext`
- A2-0320 — MarketDataUploader: Let’s use `runWithReporting` which gives some utility around logging / allowing to capture individual error and move on instead of blocking the stream
- A2-0401 — BaseAdvisoryServiceE4s: Let’s structure the endpoints like this. I missed this in prev PR, but maybe add `tenant` segment is good idea
- A2-0414 — BaseAdvisoryServiceE4s: Should we create another API object for all these tenant specific endpoints? Their logic should extract the tenant from tracing context, and use it for c...
- A2-0424 — SgInstrumentFilterManager: Maybe we can structure this trait like this
- A2-0441 — InvestorTypeFixForNonSgdInstrumentWithCpfAndSrs: better to use `Source(instrumentsToUpdate).mapAsync(...)` so that we can control the parallelism
- A2-0485 — package: I’m thinking if we want to create a case class for this instead, so we can add more fields if needed in future
- A2-0525 — HkCustomerDailyFeesCalculator: But this calculator should not split by product like that. If you see SG, except for flat rate or single fund fundsmart, they all follow same meth...
- A2-0544 — HkChargeCommunicationProjection: This logic actually exists in `InitiateFeeRedemptionCmdHandler`, it’s best we rely on sequence of events, rather than duplicating it again.
- A2-0558 — DistributionCalculatorHelperHk: Can we retry \+ fallback to entity for this, just to be on safe side?
- A2-0581 — package: Existing GoalDto continue to serve the generic usage of BE services, and “edge” usage of FE. We might add new edge B2C\*Dto for FE in future, but for now, we only need ...
- A2-0626 — AkkaHttpAuthRecipesTest: Which executionContext is this? We should probably use the one from AsyncWordSpec right?
- A2-0637 — package: I suppose this is already inside the `lazy val corePortfolioOfferingResponseSchema` so these supporting JsonSchema of Map type don’t need to be lazy anymore, but better...
- A2-0638 — package: Also, maybe let’s make the `JsonSchema[Map[TradingAccountType, SubscriptionAmountRegulation]]` follow the same approach, move it to be val inside the outer lazy val sch...
- A2-0649 — SgGoalModifySummaryBehaviour: Maybe lookup portfolio outside first? We need another lookup without tradingAccountType
- A2-0663 — ProductPortfolioRepository: Nit: can move a little closer to this method so that they stay in pair \(similar to those with stockRatio\)
- A2-0673 — GoalModifyBehaviourHelpers: throw if using map \(`_ = ...`\), or `Future.failed` if using flatmap \(`_ <- ...`\)
- A2-0707 — InstrumentMarketDataEventProcessor: Let’s wait for Future
- A2-0739 — PortfolioMonthlyChangesHelper: ```
- A2-0783 — SgRecommendedInvestmentManager: Best if we can refactor to avoid make unnecessary calls
- A2-0811 — TopicSubscriber: We should use `topicSubscriberSettings.parallelism` here?
- A2-0814 — TopicSubscriber: In the TaskTopicSubscribers, these are used to retry processing individual message \(before dropping them\). Here you’re using as config to restart the subscrip...
- A2-0816 — TopicSubscriber: [person] As discussed, it’s actually not safe to blindly increase `parallelism` here when consuming messages from same partition \(only safe for the task topic\).
- A2-0821 — ProductPortfolioRepository: Maybe we can keep this method generic, but only handle for CoreEnhanced for now…
- A2-0826 — AdvisedGoalCreateHelper: Let’s make these 3 remote calls to portfolio/composition/performance run in parallel
- A2-0830 — AdvisedGoalCreateHelper: These 3 futures are still run sequentially if written like this
- A2-0836 — CustomerStatusHelper: Can we make this change for HK too
- A2-0839 — SgGoalCreatePortfolioSummaryBehaviour: Maybe consider grouping these futures so that we can run them in parallel as much as we can. There are many futures here, can make it very...
- A2-0879 — PortfolioFundLogic: Maybe `lazy val`?
- A2-0880 — ServiceLogicImpl: Should we add to FutureUtils… sth like `withTimer(timer: Timer, => T: Future[T])` and take care of proper start stop there? I suppose we don’t need to capture ...
- A2-0881 — ServiceLogicImpl: A bit late to call with withTimer here cuz the future already started when you define above
- A2-0906 — allInvestmentGoalsPage: You can have both
- A2-0982 — SgComplianceChecker: recoverWith should just return `Future.failed(exception)`. Can you help me change for cka one as well :pray:
- A2-0991 — SgComplianceChecker: Let’s use `Future.failed` for `recoverWith`
- A2-1002 — NotifyRebalanceTradeSettlementAmendedCmdHandler: If buy trade has not started, and we amend totalSoldAmount but keeping cashReservation intact, we might run into additional cash...
- A2-1034 — AdvisedPortfolioOfferingsManager: Because `getPriceCcy` might throw, and we want all exceptions are thrown in Future so that it’s more predictable for caller. And since `getPric...
- A2-1045 — PlanCommunicationV2EventProcessor: In anticipation for more custom interpolations in future, we can change this a little to below \(similar to locale specific one\)
- A2-1047 — HkGoalCreateRequest: Can be lazy val? Same for plan upsert request
- A2-1068 — PlanTraderEventProcessor: Can we log more on how to recover from here? e.g investigate \+ manually retry OR simply cancel trade
- A2-1088 — HkGoalModifySummaryBehaviour: All of these calls can run in parallel. You can try using `FutureUtils.zip`. Should be able to find similar code for SG flow
- A2-1099 — InstrumentUpsertManagerV2: No need to create new future right?
- A2-1147 — HkGoalCreateRequest: Should all these be `lazy val`?
- A2-1161 — SgFundSmartManagerV3: Maybe just extract this to the common `FundSmartInstrumentBuilder` ?
- A2-1197 — InstrumentExportScheduler: You can just batch it here
- A2-1204 — HttpServerStartup: Should we make `route` and `rejectionHandler` available in the base Endpoints? Then we provide overloading constructors, so service doesn’t need to think too ...
- A2-1229 — HkComplianceHelperImpl: mapAsync\(2\)
- A2-1239 — DetectExpiredInvestmentRequestProcessor: [person] [person] [person] Is the below correct understanding?
- A2-1277 — HkGoalCreateRequest: Consider changing all these `def` to `lazy val` instead. No need to resolve them again.
- A2-1292 — ValidationHelpers: We can extract amount validation into a method
- A2-1294 — HkGoalCreateRequest: lazy val for these too?
- A2-1295 — ValidationHelpers: Just `Future[Done]` is sufficient. For all the methods in this class
- A2-1305 — Review: Reported non-full redemption rejection: RequestedAmount 150000 exceeded plan redeemable MV 99986.82 and full redemption threshold 96987.2154. The log blocks a request no...
- A2-1306 — CustomerStateUpdatedLogic: Maybe make them follow same style right?
- A2-1311 — DividendTopicSubscriberV3: Added comment for the AbortCmd… from transaction pov, it doesnt need to know about the possible cases of pref here. In future, we might support for ca...
- A2-1314 — BaseTradabilityChecker: How about just take goalId here?
- A2-1315 — BaseTradabilityChecker: Let’s put the same retry logic as fetchPlan
- A2-1356 — MarketDataUploader: I suppose we can fetch both of these in parallel
- A2-1364 — MarketDataUploader: I was talking about this point `It will be picked up in the future when it's available`… if missing in the middle, I don’t think current code will fill in th...
- A2-1366 — MarketDataUploader: Nit: no need to start a Source from beginning I think
- A2-1367 — MarketDataUploader: If we propagate the failure in these places, it will stop the whole flow processing. I suppose we just want to skip?
- A2-1368 — MarketDataUploader: This method doesn’t need to return Future right? I have everything resolved already
- A2-1370 — MarketDataUploader: It will propagate and stop the flow, cuz we put `Future.failed(ex)`, effectively rethrow the exception
- A2-1371 — MarketDataUploader: We log error outside in the `reconcileInstrumentsPrice` already. We can just wrap the exception here to avoid double sentry alerts
- A2-1380 — MarketDataUploader: This version will now run to completion before it returns Done, making the http endpoint waits for potentially long time.
- A2-1398 — PortfolioUnderlyingManager: If you have time, can you help us change this `await` usage to the usual for-comprehend block too? All these lookup steps can be called in parallel, ...
- A2-1399 — PortfolioUnderlyingManager: I suppose we can fetch composition and performance in parallel to save some time too
- A2-1414 — SubscriberHelpers: Avoid Option.get in general. I guess here you can write it as
- A2-1416 — PortfolioSuitabilityAnalysisRequest: As discussed, let’s not mention DPM in request type, and add it as a flag paired with each portfolioId instead, so we can reuse this for fut...
- A2-1419 — PortfolioSuitabilityAnalysisLogic: Doesn’t look like we need Future here
- A2-1453 — BaseServiceLogicImpl: Better to use Source instead of Future.sequence, but ok a goal only at most 3 plans as of now. Can extract whole of this to a method instead of just `appen...
- A2-1491 — TradeTopicSubscriber: Hmm I’m surprised we have so many `parallelism` = 2 in investment svc without the safeMapAsync… [person] speed should be fine here, we should just change t...
- A2-1502 — UpdateTradeFxConversionRequestIdCmdHandler: Are you planning to use same cmd handler for future cases of `fundingInstructions`?
- A2-1504 — TradingAccountEventProcessor: Does this actually return or it will simply assign Future\[Done\] to `brokerAccountId`?
- A2-1505 — TradingAccountEventProcessor: This is actually very dangerous if we add/move the fields around and if the type matches UUID, we won’t get any compilation error…
- A2-1509 — PlanTraderEventProcessor: Maybe we should add that support should check if the queued fx indeed not created before retrying..
- A2-1518 — HkFundSmartManager: Maybe use `InstrumentInfoDto.whitelistedGoalTypes` and check based on goal types instead? Follow similar approach for sg portfolio summary, cuz we will need ...
- A2-1521 — HkFundSmartManager: Nits: These 2 methods don’t have to return Future. We can just throw and keep return type as `Unit`
- A2-1533 — FundSmartHelper: fee <- `estimateAccessFee`
- A2-1554 — RebalanceRequestTable: We missed a `v` for version here, but it’s consistent in V4 too :sweat_smile: we will change this when we upversion  this table again in future
- A2-1557 — SgFundSmartManagerV3: Yea that was good catch. This NotFound is thrown by our own `createFuture` :see_no_evil:
- A2-1558 — FxWalletQuotationServiceImplSpec: It’s more about scaffeine behaviour, but I think it’s useful to capture this in a test
- A2-1566 — TransactionJdbcProjectionV2: Let’s not mix the naming, it can be confusing for future readers:
- A2-1606 — RebateDistributionCommunicationsManager: No need to sequence here? Just let `publishRebateDistributionPlatformNotifications` decide how to run its futures
- A2-1612 — RebateDistributionCommunicationsManager: Just Source and mapAsync these
- A2-1619 — RebateDistributionCommunicationsManager: Just Source the `customerRebates` and mapAsync to lookup instruments
- A2-1638 — RegionalCustomerTopicCustomer: Entity is keyed by goalId so would it be better to increase parallelism for goals to 4, keeping parallelism for plans at 1?
- A2-1649 — PreferredLocalLookupHelper: Can we add a base trait `PreferredLocalLookupHelper` too?
- A2-1656 — enums: I think the industry terminology is advisory and execution-only? Also I’m not too sure about naming this `AdvisoryLevel`. I think there can a 3rd mode as well, aka discre...
- A2-1676 — AdvisoryDataTranslationManagerSpec: Maybe put the one needed for the test only. Now that we have the cache to mock, for readability, maybe use English instead :rofl: 
- A2-1679 — RedemptionRequestTopicSubscriberV3: Let’s make this specific to fee redemption only, and move the `request.feeChargeDetails.isDefined` to require clause
- A2-1690 — PortfolioUnderlyingManager: Sorry [person]. I forgot we already have this fundDocuments → urlMap logic in FundDetails.toDto which takes care of returning latest version of these...
- A2-1712 — RebalanceApplication: Can you help to put a comment here to remind us about the mismatch between table version and readside version, to avoid future confusion :pray:
- A2-1731 — SgFundSmartManagerV3: At this point we don’t have any remote calls anymore, can do mapAsync\(4\) I think
- A2-1733 — SgFundSmartManagerV3: Yeah `performanceMap` already contains only that specific period type \(if any\)
- A2-1784 — HkFundSmartTemplateRecommendedLabelHelper: It’s all hard-coded, we can make these 2 Maps `lazy val` instead
- A2-1788 — InstrumentDataUpdateManagerV2: Maybe move this up so we fail faster. Also need to `throw` instead of `Future.failed` if using `=`, i.e. `Future#map`
- A3-0003 — MStar sync Futures: retry, current-DB fallback and final-error logging
- A3-0010 — ServiceLogicImpl.scala: Does this look better? ``` instrumentId .map(marketDataUploader.syncInstrumentMstarData) .getOrElse { // run in background marketDataUploader.safeSync
- A3-0018 — MAS getLatest on weekend/currency holiday: latest available rate and optional tail recursion
- A3-0026 — InstrumentV2JdbcDbHandler.scala: We don’t really need transaction for readside so we can inject db here, and return Future… it’s easier to use and mock in test if needed
- A3-0044 — ComplianceServiceException NotFound caught for unrelated scenario causes unnecessary retries
- A3-0045 — ServiceLogicImpl.scala: advisory circuit breaker timeout will kick in at 15s… do we need this long?
- A3-0046 — compliance-slowProcess identifies compliance circuit breaker and uses slowProcess config
- A3-0047 — ServiceLogicImpl.scala: recoverWith expects a Future as return type so you can use Future.failed\(ex\) instead
- A3-0048 — Compliance retry test: trust FutureUtils or override backoff for short unit tests
- A3-0055 — PortfolioOfferingResponseV2 sealed-trait concern and product-specific MAA card flow
- A3-0062 — InvestmentRequestTopicSubscriberV3.scala: Should be able to remove this throttle?
- A3-0071 — ServiceLogicImplV2.scala: This one is old code, but I think better to mapAsync so that we can control the parallelism instead of blind run with throttle… we can ignore the resu
- A3-0072 — InstrumentDataUpdateManagerV2.scala: no need for comprehend if just single future
- A3-0107 — Quarterly fee estimate avoids Kafka task: no OOMKilled and idle partition/consumer cost
- A3-0115 — ServiceLogicImpl.scala: ~~Actually the common code should be a method that takes List\[GoalDto\] and return Future\[List\[RecommendedPortfolioChangeDto\]\]~~ ~~Then customer 
- A3-0124 — ServiceLogicImpl.scala: We have utils in OptionUtils so this can be written as ``` rpcCmsWebflowIdJdbcRepository .find(portfolioId, effectiveDate) .map(_.map { entry => RpcCm
- A3-0125 — ServiceLogicImpl.scala: Same here, you don’t need to match. Can extract to reuse same toDto method as well ``` rpcCmsWebflowIdJdbcRepository .findByItemId(itemId) .map(_.map(
- A3-0143 — BaseChargeService.scala: It’s too heavy to run for all customers even for Alts. So I revert back to expecting for single customerId
- A3-0150 — Voucher wallet calculation needs full GetVoucherWalletStateCmd; entity load is bottleneck
- A3-0198 — CustomerTransactionMigrationEventProcessor.scala: You can `import com.endowus.silver.commons.utils.FutureUtils.FutureRetryExt` And use it like this ``` fut.withRetry(AlwaysRetryOnException) ```
- A3-0218 — Lagom/removed-Lagom error-serdes, shared breaker, whitelist and request-timeout verification matrix
- A3-0219 — Cross-service heavyProcess breaker collision: prefix service name and keep default-superHeavyProcess
- A3-0241 — BasePlanRecurringInvestmentScheduleManager.scala: Retry for this too, in case we have any transient error
- A3-0243 — PlanCommunicationV2EventProcessor.scala: Can we extract this communication sending to separate method so it’s easier to follow? ``` event.removalReason match { case Some(RecurringInvestmentSc
- A3-0244 — Idempotent command permits bounded AskTimeout retry
- A3-0245 — PlanCommunicationV2EventProcessor.scala: Why we need to `.map(_ => Done)` again?
- A3-0255 — RecurringInvestmentScheduleJdbcEventProcessor.scala: You’ll need for-comprehend block
- A3-0265 — UpdatedEvt old/new inserts and offset-commit failures: duplicate windows and PK alternatives
- A3-0304 — RecurringInvestmentFrequencyDetailUtilTest.scala: No future so you can just use AnyWordSpec
- A3-0310 — PlanCommunicationV2EventProcessor.scala: So we’re ok to fire and forget here?
- A3-0323 — Three-MCCY-broker creation: partial success, retry and stale active-account readside
- A3-0377 — SgPlanUpsertConfirmationBehaviour.scala: This part looks a bit weird to me, cuz these 2 requests are now independent of each other. In theory we shouldn’t have to match them together. ``` for
- A3-0378 — SgInvestmentServiceImpl.scala: Better to just inject db directly into `investmentScheduleActivePeriodJdbcRepository` and the methods can return Future instead of DBIO
- A3-0401 — InvestmentScheduleActivePeriodJdbcEventProcessor.scala: the better syntax would be ``` _ <- investmentPlan.recurringInvestmentSchedule match { case Some(schedule) => repository.upsert(...) case None => Futu
- A3-0415 — SgServiceLogicImpl.scala: For timing, we can import `TimeUtils.TimedLogger` and simply call ``` logger.logTime(context) { fut } ```
- A3-0420 — Risk-target performance example uses mapAsync2 over risks and mapAsync1 over plans
- A3-0509 — FeeChargeRequestJdbcEventProcessorV5.scala: Hmm so we also update these planProfile too. I guess it’s fine cuz this will look up latest planProfile, but still feel very expensive :sweat_smile:
- A3-0514 — PlanTimeseriesTopicSubscriber.scala: ``` val DefaultFutureRetrySettings: FutureRetrySettings = FutureRetrySettings( minBackoff = 500.milliseconds, maxBackoff = 5.seconds, randomFactor = 0
- A3-0516 — Readside TAA retry proposal5s-to10s/3 retries assumes no repeated TAA-updated event
- A3-0527 — TaxExemptionManager.scala: Would returning Future\[Boolean\] match the `isCustomerExempted` better?
- A3-0529 — Idempotent fee projection handlers with noop-catch-up then new-flow second release
- A3-0534 — InvestmentTransferEventProcessor.scala: We need to return Future to chain it here. Otherwise, event processor won’t wait for investOnce and `NotifyInvestmentProcessInitiatedCmd` to complete 
- A3-0543 — common.conf: This will increase timeout for all endpoints. should we make request timeout configurable in `EndpointExtensions#impl` using `Directives#withRequestTi
- A3-0557 — PortfolioSuitabilityAnalysisLogic.scala: How about we create a local scaffiene cache for instrument performance in this method \(i.e. invalidate all after we are done with all the `instrument
- A3-0571 — Only transient errors should throw in EventProcessor/TopicSubscriber to avoid stuck data errors
- A3-0573 — BrokerAccountTopicSubscriberCommunicationLogic.scala: Since it’s within investment svc, should we inject refProvider and just use ``` investmentRequests <- refProvider.getPlanInvestmentManagerEntityRef(UU
- A3-0594 — BrokerCommunicationV2EventProcessor.scala: Just curious, why change to def here? Wouldn’t it be simpler to val it \(let it start running\), and we simply wait for it in the for yield block \(me
- A3-0598 — BrokerAccountTopicSubscriberHandlers.scala: If we rethrow here, and it’s not transient error… the subscriber will get stuck
- A3-0604 — Alts cash-reservation remote call in projection; Kafka request/result ideal lacks trading events
- A3-0615 — Slick cleanUp proposal preserves streaming and avoids running result twice
- A3-0616 — PortfolioService.scala: This endpoint is used by Davinci? Does this actually help at all, cuz circuit breaker config should be on client side?
- A3-0687 — TransactionFxConverter.scala: Not good hide var like this \(e.g `maybeConvertedSettlementDetail` was a fut, and then reassigned as an Option How about just ``` maybeConvertedSettle
- A3-0699 — UtilityManager.scala: log error and move on to next portfolioId instead of throwing and block the whole set
- A3-0709 — SubscriberMetricsWithKamon.scala: recoverWith should return Future Use recover \+ throw or recoverWith \+ Future.failed
- A3-0711 — RebalancePlanJdbcRepository.scala: Seems identical to existing method? We can just change the old one to return Future?
- A3-0747 — PlanTimeseriesTopicSubscriber.scala: TimedLogger#logTime already logs info when the future completes. Do we still need this log?
- A3-0758 — Transaction FX conversion Futures: bounded Source.mapAsync2 proposed
- A3-0759 — TransactionFxConverter.scala: Can we rename \+ declare type for this to indicate it’s a Option\[Future\]… otherwise I feel it’s a little confusing to read this block…
- A3-0774 — FxRateHelper.scala: ``` fxRateCache .getIfPresent(fxId) .map(Future.successful) .getOrElse(loadCacheAndFind(fxId)) ``` Try to use Option more idiomatically
- A3-0786 — ReportApplication.scala: The channels are supposed to be pooled… not sure why are we wiring it here…
- A3-0792 — SftpTask pooled channel runner versus long-held connection historical failures
- A3-0799 — SftpTask.scala: Can we add a function to extract only data that we need? Returning the whole buffered reader is not good I think. Ofc being able to stream the output 
- A3-0801 — SftpMetadataChecker.scala: This returns a try. So even if the below exception is thrown, the flow doesn’t stop
- A3-0804 — SftpMetadataChecker.scala: Do we need to throttle and `parallelism` = 1? I think it’s ok to just query with `parallelism` = 2 without throttling here
- A3-0811 — AdvisedPortfolioOfferingsManager.scala: You can write this as ``` .mapAsyncUnordered(parallelism = 2) { case (portfolioId, effectiveDate) => ```
- A3-0821 — Independent dividend files: BadRequest nonretry and bounded TCP/unknown retry
- A3-0822 — Recurring failure email: actual reason, event-domain coupling and direct-publish deferral
- A3-0825 — RecurringInvestmentProcessor.scala: Can we move retry logic to `tradabilityChecker` itself, similar to complianceChecker? It’s already very cluttered here
- A3-0826 — RecurringInvestmentProcessor.scala: No we should only retry when it makes sense to… but it means the underlying service needs to tell you that. In this case, we build compliance service 
- A3-0827 — Bounded retry-all temporarily tolerated while underlying retryability contract evolves
- A3-0828 — RecurringInvestmentProcessor.scala: Oh why are we retrying again here
- A3-0830 — RecurringInvestmentProcessor.scala: Ok then can we move all that to the checkers themselves? This processor should just focus on the logic I think
- A3-0832 — RecurringInvestmentProcessor.scala: Yes, notification is “extra” in this flow. Let’s do it last, with retry \(inside the email helper\). Log error if exhaust all retries, and expose endp
- A3-0842 — HkNotificationManager.scala: Or maybe this method can just log warn and skip the customer. No point to throw?
- A3-0849 — NotificationManager.scala: You can do ``` .mapAsync(2) { case (customerData, profileData) => ... } ```
- A3-0850 — NotificationManager.scala: Looks like you don’t need for-comprehend block here
- A3-0878 — ServiceLogicImpl.scala: move this into the recover block of `retrieveFirstRowInDividendDistributionFile`?
- A3-0880 — FxRatesProjectionRepository.scala: If no streaming, then don’t need SlickSession I think
- A3-0883 — FxRatesTopicSubscriberV2.scala: This the upsert call fails, the whole future will still error, and the subscriber will retry. The `.map(_ => Done)` purely means “we are ignoring the 
- A3-0891 — Macwire inside Future sometimes misses subscribers; possible SlickReadside relation unproven
- A3-0918 — CraManager.scala: Can just log warn and move on? Same for VC below?
- A3-0924 — CraManager.scala: If we throw, we block Kafka..
- A3-0931 — HkServiceLogicImpl.scala: Oh bulk upsert for whole set of customers would be too large… either batch the source, or just upsert one by one I think…
- A3-0972 — ServiceLogicImpl.scala: we don’t actually need this for comprehend block here if it’s just one future
- A3-0975 — LagomServiceExceptionHelper.scala: I guess it’s not really required here \(and only here\)… `PrintWriter#close` will attempt to close its underlying output stream which is this `CharArr
- A3-0976 — Scala2.11 PrintWriter/CharArrayWriter no-close exception relies on noop underlying close
- A3-0977 — InstrumentMarketDataEventProcessorForMultiCcy.scala: So we keep trying until the circuit breaker resets?
- A3-0983 — Missing broker virtual-account data blocks tag and may age communication past2days
- A3-1007 — NewWealthDataUploader.scala: Do you want to add a utils method to wrap future with `.withRetry(AlwaysRetryOnException, retrySettings)` instead? We always use default retry setting
- A3-1012 — Error-contract tests: missing CRA, concurrent invest retry, instrument-down propagation
- A3-1046 — HkServiceLogicImpl.scala: We don’t need this cuz the cmd already returns Done?
- A3-1057 — KafkaTaskHelper.scala: can you guys take a quick look at this helper? I extract the retry behaviour to `FutureUtils.futureWithRetry` for reuse
- A3-1080 — CraCategoryMatcher.scala: This one is more like utils method, so let’s put it in companion object? Also we don’t need Future?
- A3-1090 — Projection transient retryWARN versus persistent lag threshold1hr and Sentry flooding
- A3-1096 — BaseServiceLogicImpl.scala: You can just use `=` if not returning a future.. It’s equivalent to `Future#map`
- A3-1099 — BaseServiceLogicImpl.scala: The 2 calls to trading and marketdata are independent of each other. If time is a concern, we can call them in parallel too, instead of sequential lik
- A3-1110 — ModifyPlanAcknowledgementsLogic.scala: Don’t need for-comprehension block if you have only one future
- A3-1126 — SimulateTradingRestrictionLogic.scala: Surprise surprise, it’s not lazy :grimacing:
- A3-1134 — QueryTradingRestrictionLogic.scala: Right ok, so we lookup for all plans, and the entity has initial empty state if no acks. Should be able to lazy this, and only lookup acks if plan has
- A3-1155 — SupportTradingRestrictionLogic.scala: Will move this to background task, return Future\[Done\] when we implement Slack integration. In this version, simply collect data and return in respo
- A3-1162 — StatementDataGenerator has documentId+statement after PDF; avoid topic relookup for comm
- A3-1177 — ChargeApplication.scala: Hmm if lazy val, and not injected anywhere, I don’t think these will get wired at all?
- A3-1205 — TradingRestrictionLogic.scala: This will not wait for the future to complete. And we wouldn’t know if it fails either…
- A3-1220 — MarketDataUploader.scala: Why do we need to separate this future?
- A3-1221 — MarketDataUploader.scala: Yeah, I can’t see the benefit of this being in separate for-comprehension block
- A3-1223 — InstrumentManager.scala: Wanna take this chance to refactor this into for-comprehension instead of async await?
- A3-1264 — Release-earmark subscriber serial1 is conservative preference, not required ordering proof
- A3-1268 — BrokerCashTransactionTopicSubscriberV2.scala: If we throw here, this subscriber will stuck on this message
- A3-1284 — ChargeApplication.scala: This one looks strange. How is it possible that this one is lazy val in SG today :open_mouth: I guess because it’s wired in `ServiceLogicImpl` ? Seem 
- A3-1293 — ConcentrationRiskValidator.scala: This duplicate pattern matching on request type seems to suggest we should break down by type earlier. Example for the simulation flow: ```scala def v
- A3-1294 — ConcentrationRiskValidator.scala: This way, for confirmation flow, the skeleton private method would accept 2 functions returning Future: * one for the investment values * another for 
- A3-1358 — CustomerAdvisoryProfileEntity.scala: Yup. Switched to another exception type for concurrent modification, and retry on it in the subscriber
- R-3336 — PlanTimeSeriesSubscriber: proposed mapAsync(1) without throttle before finding the unawaited simulation
- R-3337 — safeRenewProjectionForCustomer is started with a value binding and not awaited
- R-3338 — Decouple MV draining from simulation with a separate retry/throttle/conflate topic proposal
- R-3406 — Unit is like void, hence everything it mappable to Unit. And by extension, every Future\[Blah\] to mappable to Future\[Unit\]. We normally return Future\[a
- R-3420 — `FeeGenerator#generatePlanFeeForFullRedemption` is not “safe” and would propagate any exception. Unlike `FeeGenerator#safeGeneratePlansFeeForCustomer` whic
- R-3449 — This already returns `Future[Done]` so we don’t need this for comprehend at all? Also for timing, would you like to give `TimeUtils.TimedLogger` a try? You
- R-3450 — Since we are already in Future scope here, I normally find it better to return `Future.failed(BadRequest())` instead Also let’s add some error message, rat
- R-3454 — Future.failed versus throw in transform is a personal preference with the same effect
- R-3455 — Maybe we don’t need parallelism = 2 here, since it’s always same entity
- R-3501 — Proposal to recover force-rebalance failure after successful TAA update because a later topic message can trigger rebalance
- R-3554 — We don’t need this? As parallelism is local to mapAsync only
- R-3556 — If you prefer Exception instead, because say you expect caller to always call with valid ID… then code is little cleaner to read if we return Future.failed
- R-3558 — Portfolio stats exact-ID lookup and filter lookup both produce a List response
- R-3566 — Scala syntax question: Since you use `val syncFut`, `.runWith(Sink.ignore)` would already trigger the fire-and-forget? So we don’t need this whole for-comp
- R-3568 — Another Scala syntax question: isn’t it better to return Future.failed\(exception\) here instead of throwing?
- R-3581 — Parallel confirmation safeguards rely on UI validation and rare FE-invalid requests in this flow
- R-3587 — Goal modify futures are constructed sequentially and tested as three dependent steps

## Full source cases

## A1-0046 — Failure notification and upcoming-date update share investment-cancellation condition

**Source stance:** open-question

**Context:**

> component: investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala; operation: [INV-5741] feat(communication, investment): Update Recurring Investment Failure Notification; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Customer should be informed and date incremented after deciding not to proceed

**Source-preserving request, proposal, or question:**

> `notifyFailedInvestmentRequest` and `updateNextUpcomingDateForPlan` should be triggered by same condition? basically we have decided not to proceed with the investment, and therefore we should let the customer know and increment the date

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:48 · comment 822581358 · PR 14066 · 2026-07-07

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala`

**Explicit source context (pr_title):**

> [INV-5741] feat(communication, investment): Update Recurring Investment Failure Notification

## A1-0047 — Chain recurring-investment futures

**Source stance:** open-question

**Context:**

> component: investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala; operation: [INV-5741] feat(communication, investment): Update Recurring Investment Failure Notification; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> These futures should be chained?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:49 · comment 822582032 · PR 14066 · 2026-07-07

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala`

**Explicit source context (pr_title):**

> [INV-5741] feat(communication, investment): Update Recurring Investment Failure Notification

**Evidence:** anon-1.jsonl:49 · comment 822582032 · PR 14066 · 2026-07-07

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala`

**Explicit source context (hunk):**

> +            for {
> +              _ <- notifyFailedInvestmentRequest(investmentPlan, dateToUse, schedule, validationErrors)
> +              _ <- updateNextUpcomingDateForPlan(dateToUse, investmentPlan)
> +            } yield ValidationFailed(validationErrors)
> +          } else {
> +            Future.successful(ValidationFailed(validationErrors))
> +          }
> +        } yield validationOutcome
> +      }

## A1-0110 — Avoid another remote instrument-service fetch in PlanTopicSubscriber

**Source stance:** requested-change

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/PlanTopicSubscriber.scala; operation: [INV-5597] feat(advisory compliance goal instrument investment rebalance trading): add etf and car ack; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> ideally we don’t want fetch from remote instrument svc again

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:113 · comment 814803409 · PR 13979 · 2026-06-19

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/PlanTopicSubscriber.scala`

**Explicit source context (pr_title):**

> [INV-5597] feat(advisory compliance goal instrument investment rebalance trading): add etf and car ack

**Evidence:** anon-1.jsonl:113 · comment 814803409 · PR 13979 · 2026-06-19

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/PlanTopicSubscriber.scala`

**Explicit source context (hunk):**

> +          newHasTypes <- hasInstrumentTypes(newInstruments, checkEtf = false, checkSip = true)
> +          _ <- if (currentHasTypes.hasSip && !newHasTypes.hasSip) {
>              val timestamp = msg.rebalanceRequest.map(_.requestedAt.toInstant).getOrElse(dateTimeProvider.now.toInstant)
> -            removeSipAck(Seq(msg.planId), PlanTaaUpdatedFromSipToNonSipInstruments, timestamp)
> +            removeAck(Seq(msg.planId), PlanTaaUpdatedFromSipToNonSipInstruments, timestamp)
>            } else Future.successful(Done)
>          } yield Done
>        } else {

## A1-0132 — Use Future.failed in SG compliance checker and fix HK too

**Source stance:** requested-change

**Context:**

> component: redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/utils/SgComplianceChecker.scala; operation: [INV-5597] feat(advisory compliance goal instrument investment rebalance trading): add etf and car ack; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Future.failed
> 
> Help me fix for HK too

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:135 · comment 816264219 · PR 13979 · 2026-06-23

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/utils/SgComplianceChecker.scala`

**Explicit source context (pr_title):**

> [INV-5597] feat(advisory compliance goal instrument investment rebalance trading): add etf and car ack

**Evidence:** anon-1.jsonl:135 · comment 816264219 · PR 13979 · 2026-06-23

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/utils/SgComplianceChecker.scala`

**Explicit source context (hunk):**

> +      .recoverWith {
> +        case ex =>
> +          val msg = s"Compliance Service call for API checkCustomerTradingRestrictionV3 failed for customer [$customerId]"
> +          logger.error(msg, ex)
> +          Future.failed(RedemptionSvcException(msg, RedemptionSvcErrorType.COMPLIANCE_SERVICE_ERROR))
> +      }
> +  }
> +}
> +

## A1-0136 — Resolve AAA through queryLatestDailyMarketValueByPlanId or getLivePlanInstrumentBalances

**Source stance:** suggestion

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/SgTradingRestrictionLogicImpl.scala; operation: [INV-5597] feat(advisory compliance goal instrument investment rebalance trading): add etf and car ack; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Composition fetches unnecessary underlying holdings

**Source-preserving request, proposal, or question:**

> Composition svc would fetch all the underlying holding data as well, I think that’s too much wasted effort.
> 
> For AAA, I think we can use timeseries `queryLatestDailyMarketValueByPlanId` \(same API used by this composition endpoint\) or trading `getLivePlanInstrumentBalances` \(entity\). Need to check for positive `holdingUnits`.
> 
> But this is not guaranteed to contain TAA instruments tho, so we still add separately

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Check positive holdingUnits; AAA need not contain all TAA instruments, so add TAA separately.

**Evidence:** anon-1.jsonl:139 · comment 816425616 · PR 13979 · 2026-06-23

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/SgTradingRestrictionLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-5597] feat(advisory compliance goal instrument investment rebalance trading): add etf and car ack

## A1-0156 — Validate corporate rules before fetching existing profile

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/B2bCorporateRulesManager.scala; operation: BB-3804: add group-level public-access profile for B2B FundSmart builder; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> This validation should happen before we fetch exiting profile

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:161 · comment 819134812 · PR 13986 · 2026-06-29

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/B2bCorporateRulesManager.scala`

**Explicit source context (pr_title):**

> BB-3804: add group-level public-access profile for B2B FundSmart builder

**Evidence:** anon-1.jsonl:161 · comment 819134812 · PR 13986 · 2026-06-29

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/B2bCorporateRulesManager.scala`

**Explicit source context (hunk):**

> +      maybeProfile <- corporateProfileJdbcRepository.findById(profileId)
> +      existingIds <- extractPublicAccessInstrumentIds(groupId, maybeProfile).map(_.toSet)
> +      _ <- {
> +        val overlapping = request.instrumentIdsForAddition intersect request.instrumentIdsForRemoval
> +        if (overlapping.nonEmpty) Future.failed(BadRequest(s"Instrument IDs $overlapping appear in both addition and removal sets"))
> +        else Future.successful(Done)
> +      }
> +
> +      newIds = (existingIds

## A1-0177 — Sort and createPage in one Future.map and companion Ordering for transaction rows

**Source stance:** suggestion

**Context:**

> component: report-impl/src/main/scala/com/endowus/silver/report/impl/statementv3/logic/presentation/pages/CompletedTransactionsPageGenerator.scala; operation: [INV-5210, INV-5211, INV-5916] Feat/presentation completed processing transaction; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Avoid tuple allocation for each entry

**Source-preserving request, proposal, or question:**

> nit: can sort and createPage in single Future.map
> 
> Better to create Ordering in companion object of `CompletedTransactionRow` and `ProcessingTransactionRow` so we don’t have to create the tuple for all entries

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:183 · comment 815848529 · PR 14029 · 2026-06-22

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statementv3/logic/presentation/pages/CompletedTransactionsPageGenerator.scala`

**Explicit source context (pr_title):**

> [INV-5210, INV-5211, INV-5916] Feat/presentation completed processing transaction

## A1-0193 — Assign future to val to start parallel with orderRowsFut

**Source stance:** requested-change

**Context:**

> component: report-impl/src/main/scala/com/endowus/silver/report/impl/statementv3/logic/presentation/pages/ProcessingTransactionPresentationBehaviour.scala; operation: [INV-5210, INV-5211, INV-5916] Feat/presentation completed processing transaction; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> This can be assigned to val so that it starts in parallel with `orderRowsFut`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:199 · comment 816022266 · PR 14029 · 2026-06-22

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statementv3/logic/presentation/pages/ProcessingTransactionPresentationBehaviour.scala`

**Explicit source context (pr_title):**

> [INV-5210, INV-5211, INV-5916] Feat/presentation completed processing transaction

**Evidence:** anon-1.jsonl:199 · comment 816022266 · PR 14029 · 2026-06-22

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statementv3/logic/presentation/pages/ProcessingTransactionPresentationBehaviour.scala`

**Explicit source context (hunk):**

> +    // Synthetic buy leg on the target goal only exists when (a) the redemption is part of an
> +    // investment-transfer (target details present) AND (b) ProcessingInvestmentValueBehaviour
> +    // emitted a synthetic movement for it. Exactly one is expected; more is a data-contract break.
> +    val investmentTransferBuySyntheticRows: Future[List[ProcessingTransactionRow]] = {
> +      val tx = input.tx
> +      (lookup.syntheticsByReferenceRowId.get(tx.id), tx.investmentTransferTargetDetails) match {
> +        case (Some(movements), Some(targetDetails)) =>
> +          val movement = singleSyntheticMovement(tx.id, movements, "investment-transfer buy")
> +          for {

## A1-0241 — SG rebalance advisory request fetches unnecessary extra data

**Source stance:** observed-defect

**Context:**

> component: rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/SgServiceLogicImpl.scala; operation: [INV-5700] feat(goal, rebalance): NVM goal details page changes; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> This is very heavy usage. And we shouldnt need all the extra data from advisory

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:248 · comment 809622387 · PR 13856 · 2026-06-11

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/SgServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-5700] feat(goal, rebalance): NVM goal details page changes

## A1-0261 — Instrument upsert uses Future.failed

**Source stance:** requested-change

**Context:**

> component: instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentUpsertManagerV2.scala; operation: [INV-5597] feat(instrument): add mic in instrument; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Use Future.failed

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:268 · comment 809592818 · PR 13945 · 2026-06-11

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentUpsertManagerV2.scala`

**Explicit source context (pr_title):**

> [INV-5597] feat(instrument): add mic in instrument

**Evidence:** anon-1.jsonl:268 · comment 809592818 · PR 13945 · 2026-06-11

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentUpsertManagerV2.scala`

**Explicit source context (hunk):**

> }
>  
> +    request.fundDetails.mic match {
> +      case Some(mic) if !MicAndExchangeNameMapping.AllowedMic.contains(mic) =>
> +        Future.failed(throw BadRequest(s"No exchange name configured for mic $mic"))
> +      case _ => // valid or no MIC â proceed
> +    }
> +
>      for {

## A1-0286 — TransactionsDataGenerator owns two-phase ordering and accepts concrete List

**Source stance:** suggestion

**Context:**

> component: report-impl/src/main/scala/com/endowus/silver/report/impl/statementv3/logic/data/TransactionsDataGenerator.scala; operation: [INV-5784] Feat/transaction mapping; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Passing Futures obscures orchestrator responsibility

**Source-preserving request, proposal, or question:**

> Not sure why these methods need to accept a Future.
> 
> Overall, we can only call this `TransactionsDataGenerator` as 2-phase orchestrator if it’s the one deciding the ordering
> 
> ```
> def createTransactionsData(transactions: List[TransactionDto])(start: LocalDate, end: LocalDate): TransactionsData = {
>   // 2 steps here
> }
> ```
> 
> ‌
> 
> The step methods can be `private[data]` and visible for testing

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Step methods can be private[data] for tests.

**Evidence:** anon-1.jsonl:293 · comment 798921234 · PR 13849 · 2026-05-20

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statementv3/logic/data/TransactionsDataGenerator.scala`

**Explicit source context (pr_title):**

> [INV-5784] Feat/transaction mapping

## A1-0303 — Fetch only validInstruments in both regions

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/HkFundSmartInstrumentBuilder.scala; operation: [INV-5558] feat(advisory): add performance based on daily market data; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Only need to fetch for `validInstruments` right? Same for SG

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:310 · comment 794521203 · PR 13698 · 2026-05-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/HkFundSmartInstrumentBuilder.scala`

**Explicit source context (pr_title):**

> [INV-5558] feat(advisory): add performance based on daily market data

**Evidence:** anon-1.jsonl:310 · comment 794521203 · PR 13698 · 2026-05-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/HkFundSmartInstrumentBuilder.scala`

**Explicit source context (hunk):**

> (validInstruments, performancesByInstrument) <- filterValidInstrumentsByPerformance(context.applicableInstruments, context.existingInstrumentIds)
>        annualYieldsByInstrument <- fetchInstrumentsAnnualYield(validInstruments)
>        suitabilityWarningsByInstrument <- fetchSuitabilityWarningsByInstrument(maybeCustomerId, validInstruments)
> +      performanceWithDailyMarketData <- instrumentDailyPerformanceCache.getCachedInstrumentPerformancesMetrics(validInstruments.map(_.id))
>        instrumentsWithDerivedTags = validInstruments.map(addDerivedTagsV2(_, HkFundSmartInstrumentBuilder.blacklistedInvestorTypes, useInstrumentTypeForAssetClassFilter))
>        allPossibleTagsMap <- buildAllPossibleTagsMap(instrumentsWithDerivedTags, HkFundSmartInstrumentBuilder.blacklistedInvestorTypes, maybeLocale)
>        fundSmartInstruments <- Source(instrumentsWithDerivedTags.toList)

## A1-0341 — Log access failures with outer recoverWith for all user roles

**Source stance:** requested-change

**Context:**

> component: bff-impl/src/main/scala/com/endowus/silver/bff/impl/auth/guards/GuardsHandlerLogic.scala; operation: [BB-3314]: Add ringfencing profile management APIs for UOBKH; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> And then log outside using `recoverWith` \(similar to other methods\), so that we have the logs for all cases even when other user roles try to access

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:348 · comment 788837266 · PR 13420 · 2026-04-27

Source path: `bff-impl/src/main/scala/com/endowus/silver/bff/impl/auth/guards/GuardsHandlerLogic.scala`

**Explicit source context (pr_title):**

> [BB-3314]: Add ringfencing profile management APIs for UOBKH

## A1-0359 — Use Akka Source destinationProfileIds mapAsync with concurrency 2 or 4

**Source stance:** suggestion

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/CorporateRulesManager.scala; operation: [BB-3314]: Add ringfencing profile management APIs for UOBKH; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Use akka stream `Source(destinationProfileIds).mapAsync(2/4) { ... }`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:366 · comment 789369473 · PR 13420 · 2026-04-28

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/CorporateRulesManager.scala`

**Explicit source context (pr_title):**

> [BB-3314]: Add ringfencing profile management APIs for UOBKH

## A1-0365 — Do not fetch retail separately

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/CorporateRulesManager.scala; operation: [BB-3314]: Add ringfencing profile management APIs for UOBKH; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> No need to fetch retail separately

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:372 · comment 789368017 · PR 13420 · 2026-04-28

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/CorporateRulesManager.scala`

**Explicit source context (pr_title):**

> [BB-3314]: Add ringfencing profile management APIs for UOBKH

## A1-0383 — Fetch only new exclusive IDs if both validations apply only there

**Source stance:** open-question

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/BffCorporateRulesManager.scala; operation: [BB-3314]: Add ringfencing profile management APIs for UOBKH; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> So we have 2 validations, but they are both applicable to only the new exclusive. Why are we fetching for the new restrictive as well?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:390 · comment 791864464 · PR 13420 · 2026-05-04

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/BffCorporateRulesManager.scala`

**Explicit source context (pr_title):**

> [BB-3314]: Add ringfencing profile management APIs for UOBKH

## A1-0384 — Use instrumentCache getLatestInstruments to bypass cache without duplicating grouping

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/BffCorporateRulesManager.scala; operation: [BB-3314]: Add ringfencing profile management APIs for UOBKH; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s use the instrumentCache? You can use getLatestInstruments if you want to bypass the cache, but let’s not repeat these grouping logic

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:391 · comment 791867589 · PR 13420 · 2026-05-04

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/BffCorporateRulesManager.scala`

**Explicit source context (pr_title):**

> [BB-3314]: Add ringfencing profile management APIs for UOBKH

## A1-0398 — Reuse allNewInstruments or move exclusiveAdditions validation up front

**Source stance:** suggestion

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/B2bCorporateRulesManager.scala; operation: [BB-3314]: Add ringfencing profile management APIs for UOBKH; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> I suppose we can take from the same `allNewInstruments` below, if the intention is to reduce number of calls to instrument svc.
> 
> Otherwise, if we want to fetch just the `exclusiveAdditions` here explicitly, then we might as well move this validation all the way up front

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:405 · comment 792385180 · PR 13420 · 2026-05-05

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/B2bCorporateRulesManager.scala`

**Explicit source context (pr_title):**

> [BB-3314]: Add ringfencing profile management APIs for UOBKH

## A1-0403 — Compute reusable value once after fetching source, outside destination loop

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/B2bCorporateRulesManager.scala; operation: [BB-3314]: Add ringfencing profile management APIs for UOBKH; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s assign this to val after we fetch source. No need to repeat for every destination

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:410 · comment 792399161 · PR 13420 · 2026-05-05

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/B2bCorporateRulesManager.scala`

**Explicit source context (pr_title):**

> [BB-3314]: Add ringfencing profile management APIs for UOBKH

**Evidence:** anon-1.jsonl:410 · comment 792399161 · PR 13420 · 2026-05-05

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/B2bCorporateRulesManager.scala`

**Explicit source context (hunk):**

> +        for {
> +          tenants <- tenantService.getByTenantIds(GetTenantsByIdsRequest(allTenantIds.toSet))
> +          groupIds = tenants.map(_.groupId).toSet
> +
> +          _ <- if (groupIds.size > 1)
> +            Future.failed(BadRequest(s"Source and destination tenants must all belong to the same group. Found groups: $groupIds"))
> +          else Future.unit
> +
> +          result <- Source(request.destinationProfileIds)

## A1-0413 — Use rule service from getAllWhitelistedInstruments for RF summaries

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/B2bCorporateRulesManager.scala; operation: [BB-3314]: Add ringfencing profile management APIs for UOBKH; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Current method fetches excessive data; applies to overview too

**Source-preserving request, proposal, or question:**

> This method actually fetches a lot more things than we need. Now we have move all the resolve logic to rule service, we can just use it directly, starting from `getAllWhitelistedInstruments`
> 
> Same for `getTenantRingfencingProfilesOverview`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:420 · comment 793860754 · PR 13420 · 2026-05-07

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/B2bCorporateRulesManager.scala`

**Explicit source context (pr_title):**

> [BB-3314]: Add ringfencing profile management APIs for UOBKH

## A1-0418 — Move instrument-fetching logic down to fetch once

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/B2bCorporateRulesManager.scala; operation: [BB-3314]: Add ringfencing profile management APIs for UOBKH; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Inside we are fetching instruments, it’s better to move this is down so we fetch once

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:425 · comment 793858582 · PR 13420 · 2026-05-07

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/B2bCorporateRulesManager.scala`

**Explicit source context (pr_title):**

> [BB-3314]: Add ringfencing profile management APIs for UOBKH

**Evidence:** anon-1.jsonl:425 · comment 793858582 · PR 13420 · 2026-05-07

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/B2bCorporateRulesManager.scala`

**Explicit source context (hunk):**

> +  def upsertTenantRingfencingProfile(tenantId: UUID, request: UpsertTenantRingfencingProfileRequest): Future[Done] = {
> +    logger.info(s"upserting tenant profile [$tenantId], requestedBy [${request.requestedBy}]")
> +    for {
> +      // Only validate additions against the group ceiling â removals and carry-over instruments must not be blocked
> +      // by stale group config changes (e.g. an existing tenant instrument later restricted at the group level).
> +      _ <- validateTenantInstrumentsSubsetOfGroup(tenantId, request.specificInstrumentIdsForAddition)
> +
> +      maybeProfile <- corporateProfileJdbcRepository.findById(tenantId.toString)
> +      existingRules <- validateAndExtractBespokeRules(s"Tenant profile [$tenantId]", maybeProfile) {

## A1-0423 — Consider withRetry on FX lookup

**Source stance:** suggestion

**Context:**

> component: report-impl/src/main/scala/com/endowus/silver/report/impl/statementv3/logic/data/FxRatesDataGenerator.scala; operation: [INV-5206] feat(report, marketdata): fx rates for statements v3 and market data fx api; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Maybe add withRetry?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:430 · comment 797280478 · PR 13816 · 2026-05-15

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statementv3/logic/data/FxRatesDataGenerator.scala`

**Explicit source context (pr_title):**

> [INV-5206] feat(report, marketdata): fx rates for statements v3 and market data fx api

**Evidence:** anon-1.jsonl:430 · comment 797280478 · PR 13816 · 2026-05-15

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statementv3/logic/data/FxRatesDataGenerator.scala`

**Explicit source context (hunk):**

> +
> +          val baseCcys = keys.map(_.baseCcy).toList.distinct
> +
> +          marketDataService
> +            .getLatestFxRatesInRange(baseCcys, firstKey.quoteCcy, startDate = firstKey.endDate.minusDays(LookBackPeriodInDays), endDate = firstKey.endDate)
> +            .withRetry(AlwaysRetryOnException, DefaultFutureRetrySettings)
> +            .map { resultMap =>
> +              keys.flatMap { key =>
> +                resultMap.get(key.baseCcy).map(dto => key -> dto)

## A1-0431 — Retry until investmentTransferId resolves in trading

**Source stance:** requested-change

**Context:**

> component: transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/InvestmentTransferHelper.scala; operation: [INV-5707] adds data model and subscriber for igt flag; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Present ID implies record should exist; eventual-consistency miss must not become None

**Source-preserving request, proposal, or question:**

> If `investmentTransferId` exist in the request, then we must be able to find right? If not found in trading, then maybe some EC problem, and we should keep retrying until we find it instead of giving up and setting None?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:438 · comment 794546030 · PR 13824 · 2026-05-08

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/InvestmentTransferHelper.scala`

**Explicit source context (pr_title):**

> [INV-5707] adds data model and subscriber for igt flag

## A1-0447 — Future reset commands need completion logging and failure handling

**Source stance:** explanation

**Context:**

> component: charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/EamProfileManager.scala; operation: Resolve INV-5291: Eam profile validation integrations, fix up table name; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Commands can fail or be skipped by pod restart; current mapping delete prevents lookup afterward

**Source-preserving request, proposal, or question:**

> next PR: we should log completion of these reset cmd, and they actually can fail \(or skipped if pod restarts\)
> 
> For now, it’s ok-ish because once `feeTieringProfileMappingJdbcHandler.delete` goes thru, we won’t look up the plan instructions

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:454 · comment 795207671 · PR 13798 · 2026-05-11

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/EamProfileManager.scala`

**Explicit source context (pr_title):**

> Resolve INV-5291: Eam profile validation integrations, fix up table name

## A1-0497 — Log benchmark-fetch failure after retry and continue fund onboarding

**Source stance:** requested-change

**Context:**

> component: instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentDataUpdateManagerV2.scala; operation: Resolve INV-5219: Changes for benchmark retrieval logic; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Invalid MStar IDs or failed lookup should not block onboarding; override or resync later

**Source-preserving request, proposal, or question:**

> I have seen some benchmark fails here, and effectively blocks the fund onboarding. I think we should handle if we cannot fetch the benchmark info here after retry or if MStar actually return “invalid id” or sth along that line, we should just error and move on. We can always override or sync again afterwards

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:504 · comment 740613091 · PR 13204 · 2026-01-19

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentDataUpdateManagerV2.scala`

**Explicit source context (pr_title):**

> Resolve INV-5219: Changes for benchmark retrieval logic

## A1-0528 — Fetch MStar basic info with mapAsync(2), id tuple, Sink.seq and toMap

**Source stance:** requested-change

**Context:**

> component: instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentDataUpdateManagerV2.scala; operation: Feat/INV-4792 update stitch details minimal request payload; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Why are we creating a map like this? Should just be
> 
> ```scala
> .mapAsync(2)(id => mstarApiService.getFundShareClassBasicInfo(id).map(id -> _))
> .runWith(Sink.seq)
> .map(_.toMap)
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:535 · comment 778127381 · PR 13640 · 2026-04-06

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentDataUpdateManagerV2.scala`

**Explicit source context (pr_title):**

> Feat/INV-4792 update stitch details minimal request payload

## A1-0544 — Use getAdvisedPortfolioSummary directly

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/TenantAwarePortfolioManager.scala; operation: [BB-3201] feat(advisory):Update FA portfolio-builder summary; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Already contains response and same performance cache logic; inception check needs no remote fetch

**Source-preserving request, proposal, or question:**

> No let’s just use `AdvisedGoalCreateHelper.getAdvisedPortfolioSummary` directly
> 
> * It has everything you need
> * `computePerformanceData` is the same logic as `AdvisedPortfolioPerformanceCache`, so essentially we only waste some time checking the instrument inception date - but that doesn’t require any remote fetching
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:551 · comment 778117138 · PR 13126 · 2026-04-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/TenantAwarePortfolioManager.scala`

**Explicit source context (pr_title):**

> [BB-3201] feat(advisory):Update FA portfolio-builder summary

## A1-0554 — Pass fetched InstrumentInfoDto instead of refetching

**Source stance:** requested-change

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; operation: Feat/INV-5126 stitch source add marketdata; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** All callers already have full instrument

**Source-preserving request, proposal, or question:**

> Instrument is re-fetched above, so let’s just use it directly
> 
> You can refactor so that this method expects full `InstrumentInfoDto` instead, since its callers all already fetch the instrument

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:561 · comment 778131744 · PR 13629 · 2026-04-06

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> Feat/INV-5126 stitch source add marketdata

## A1-0564 — Fetch goals with includePlans false or directly use goalJdbcRepo

**Source stance:** requested-change

**Context:**

> component: goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/GoalCommunicationV2EventProcessor.scala; operation: BB-3188 auto rebalncing toggle; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> refactor to pass includePlans = false or just use goalJdbcRepo directly

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:571 · comment 776068228 · PR 13477 · 2026-03-31

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/GoalCommunicationV2EventProcessor.scala`

**Explicit source context (pr_title):**

> BB-3188 auto rebalncing toggle

**Evidence:** anon-1.jsonl:571 · comment 776068228 · PR 13477 · 2026-03-31

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/GoalCommunicationV2EventProcessor.scala`

**Explicit source context (hunk):**

> +          shouldTriggerFirstGoalComm = shouldTriggerFirstGoalNotification(goals, goal)
> +          _ <- if (!shouldTriggerFirstGoalComm) {
> +            logger.info(s"[GoalCommunicationV2Projection] Not first goal. Skipping email for customerId=[${goal.customerId}], goalId=[$goalId]")
> +            Future.successful(Done)
> +          } else {
> +            baseServiceLogicImpl.getGoalById(goalId).flatMap { goalDto =>
> +              b2bNotificationManager
> +                .sendAutoRebalancingInitialStatusEmailNotification(clientData, goalDto)
> +                .map(_ => Done)

## A1-0567 — Use event.goal instead of refetching entire goal

**Source stance:** requested-change

**Context:**

> component: goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/GoalCommunicationV2EventProcessor.scala; operation: BB-3188 auto rebalncing toggle; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> No need to fetch whole goal again? We should have everything we need in the current `goal = event.goal`?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:574 · comment 776615078 · PR 13477 · 2026-04-01

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/GoalCommunicationV2EventProcessor.scala`

**Explicit source context (pr_title):**

> BB-3188 auto rebalncing toggle

## A1-0585 — Avoid advisory-projection-simulation remote chain for simple compounding

**Source stance:** open-question

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/sg/SgGoalCreateInvestmentSummaryBehaviour.scala; operation: [PG-1948] feat(advisory) Income projection; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> What exactly will this gives? Just normal interest compounding? If so, do we really need advisory → projection → simulation for that?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:592 · comment 775507030 · PR 13581 · 2026-03-30

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/sg/SgGoalCreateInvestmentSummaryBehaviour.scala`

**Explicit source context (pr_title):**

> [PG-1948] feat(advisory) Income projection

## A1-0603 — Use recover with Seq.empty without wrapping Future

**Source stance:** requested-change

**Context:**

> component: transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/TransactionQueryLogic.scala; operation: Feat/INV-5336 enable rrt redemption; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** No further asynchronous fetch

**Source-preserving request, proposal, or question:**

> We are not fetching anything else, so `recover` and `Seq.empty` is sufficient. Don’t need to wrap another Future

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:610 · comment 767123735 · PR 13472 · 2026-03-13

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/TransactionQueryLogic.scala`

**Explicit source context (pr_title):**

> Feat/INV-5336 enable rrt redemption

## A1-0606 — Retry needs deferred rather than eager evaluation

**Source stance:** observed-defect

**Context:**

> component: transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/TransactionQueryLogic.scala; operation: Feat/INV-5336 enable rrt redemption; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> This cannot be eager right? Otherwise the retry won’t work

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:613 · comment 773342601 · PR 13472 · 2026-03-25

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/TransactionQueryLogic.scala`

**Explicit source context (pr_title):**

> Feat/INV-5336 enable rrt redemption

**Evidence:** anon-1.jsonl:613 · comment 773342601 · PR 13472 · 2026-03-25

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/TransactionQueryLogic.scala`

**Explicit source context (hunk):**

> +    transactionRepository.findAllByStatus(status).map(_.map(Transaction.toDto).toList).map(TransactionListDto(_))
> +  }
> +
> +  private def loadUpstreamUpdates[RrtReq, Status, TxnDto](
> +    fetchUpstream: => Future[Seq[RrtReq]],
> +    context: String,
> +    collectRequests: PartialFunction[RrtReq, (RrtReq, Status)],
> +    buildTransaction: (RrtReq, Status) => Future[TxnDto]
> +  ): Future[List[TxnDto]] = {

## A1-0620 — Retry only inner safeUploadMonthlyChanges without refetching instrument

**Source stance:** requested-change

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; operation: Feat/INV-5489 update stitch details endpoint; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Just retry in the inner `safeUploadMonthlyChanges`, no need fetch instrument again?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:627 · comment 774418849 · PR 13571 · 2026-03-27

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> Feat/INV-5489 update stitch details endpoint

**Evidence:** anon-1.jsonl:627 · comment 774418849 · PR 13571 · 2026-03-27

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (hunk):**

> } yield Done
>    }
>  
> -  def safeUploadMonthlyChanges(instrument: InstrumentInfoDto, stitchData: Boolean, forceUpload: Option[Boolean]): Future[Done] = {
> +  private[utils] def safeUploadMonthlyChangesWithFallback(instrument: InstrumentInfoDto, stitchData: Boolean, forceUpload: Option[Boolean]): Future[Done] = {
> +    val instrumentId = instrument.id
> +    uploadMonthlyChanges(instrument, stitchData = stitchData, forceUpload = forceUpload)
> +      .recoverWith {
> +        case e: MarketDataSvcException if e.errorType == MarketDataSvcErrorType.INCOMPLETE_DATA && stitchData && !forceUpload.contains(true)=>

## A1-0621 — Recover only safeUploadMonthlyChanges rather than full method

**Source stance:** requested-change

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; operation: Feat/INV-5489 update stitch details endpoint; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Ok I see what you’re trying to do, but still, we only need to recover when calling `safeUploadMonthlyChanges`, not the whole method

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:628 · comment 774419232 · PR 13571 · 2026-03-27

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> Feat/INV-5489 update stitch details endpoint

## A1-0625 — Private upload fallback retries without stitching then recovers typed and unexpected failures

**Source stance:** suggestion

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; operation: Feat/INV-5489 update stitch details endpoint; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> A bit messy to catch this 2 times. Since the inner method is actually private and only used by this method, how about this
> 
> ```scala
> def safeUploadMonthlyChanges(instrumentId, stitchData, forceUpload): Future[Done] = {
>   for {
>     instrument <- fetch
>     _ <- if (support) {
>       safeUploadMonthlyChangesWithFallback(instrument, stitchData, forceUpload)
>     } else {
>       ...
>     }
>   }
> }
> 
> private def safeUploadMonthlyChangesWithFallback(instrument, stitchData, forceUpload): Future[Done] = {
>   safeUploadMonthlyChanges(instrument, stitchData, forceUpload)
>     .recoverWith {
>       case incomplete error =>
>         logger.error("....cannot, retrying without stitch")
>         safeUploadMonthlyChanges(instrument, stitchData = false, forceUpload)
>     }
>     .recover {
>       case marketdata ex =>
>         logger.info
>         Done
>       case ex =>
>         logger.error
>         Done
>     }
> }
> 
> private def safeUploadMonthlyChanges(instrument, stitchData, forceUpload): Future[Done] = {
>   // don't recover here
> }
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Inner actual upload must not recover; fetch instrument once and avoid double catches.

**Evidence:** anon-1.jsonl:632 · comment 774475941 · PR 13571 · 2026-03-27

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> Feat/INV-5489 update stitch details endpoint

## A1-0626 — Retry only incomplete error with stitch true and force false

**Source stance:** open-question

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; operation: Feat/INV-5489 update stitch details endpoint; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Only retry if incomplete && stitch && !force ?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:633 · comment 774498970 · PR 13571 · 2026-03-27

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> Feat/INV-5489 update stitch details endpoint

**Evidence:** anon-1.jsonl:633 · comment 774498970 · PR 13571 · 2026-03-27

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (hunk):**

> +  private[utils] def safeUploadMonthlyChangesWithFallback(instrument: InstrumentInfoDto, stitchData: Boolean, forceUpload: Option[Boolean]): Future[Done] = {
> +    val instrumentId = instrument.id
> +    uploadMonthlyChanges(instrument, stitchData = stitchData, forceUpload = forceUpload)
> +      .recoverWith {
> +        case e: MarketDataSvcException if e.errorType == MarketDataSvcErrorType.INCOMPLETE_DATA && stitchData && !forceUpload.contains(true)=>
> +          logger.error(s"MarketDataSvcException (INCOMPLETE_DATA) while uploading the all monthly changes for instrument $instrumentId with stitchData = true. Retry with stitchData = false", e)
> +          uploadMonthlyChanges(instrument, stitchData = false, forceUpload = forceUpload)
> +      }
> +      .recover {

## A1-0640 — MStar no-doc behavior differs by MStar ID and ISIN

**Source stance:** explanation

**Context:**

> component: instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/MstarInstrumentDocumentManager.scala; operation: [INV-4814] feat(instrument): MStar fund docs enhancements; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** ISIN empty payload can mean no docs or transient failure; retry may later succeed

**Source-preserving request, proposal, or question:**

> So MStar behaviour is quite funny:
> 
> * using MStar and no docs → it returns proper xml without empty node
> * using ISIN and no docs → it returns empty response → cause MorningstarResponseParsingException
> 
> Problem is sometime, some error or whatever on their end, it still returns empty response, hence we want to retry \(I have seen examples of this while testing\)
> 
> ‌
> 
> Now if the http call itself fails, ideally we also want to retry, but last time it coincides with MStar being killed. Still not sure on the root cause, so I’m reluctant to retry here.
> 
> But yes, ideally, we should just retry regardless

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- HTTP retry historically coincided with MStar process killed; root cause uncertain; ideally retry both.

**Evidence:** anon-1.jsonl:647 · comment 765887710 · PR 13460 · 2026-03-11

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/MstarInstrumentDocumentManager.scala`

**Explicit source context (pr_title):**

> [INV-4814] feat(instrument): MStar fund docs enhancements

## A1-0641 — Trust returned MStar doc per type/locale; retain existing only absent group

**Source stance:** explanation

**Context:**

> component: instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/MstarInstrumentDocumentManager.scala; operation: [INV-4814] feat(instrument): MStar fund docs enhancements; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** MStar can remove newest docs; rare source disparity and ambiguous empty responses

**Source-preserving request, proposal, or question:**

> Yea the aggregate logic will follow MStar always, as long as it returns something. We only retain existing MStar doc if somehow MStar doesn’t return for that docType\+locale group.
> 
> The risk of what you said is there, but:
> 
> * We already retry \(I’ll change to retry for both exception type, only skip if sth else unexpected\)
> * Most of the time, the 2 sources match. Only for some rare cases, they have disparity
> * And the thing is, sometimes indeed MStar remove newest docs. It could be their mistake but it’s easier for us to follow them and raise to MStar to correct their data, instead of us trying to maintain something we don’t own \(I think\)
> 
> ‌
> 
> Ideally, I would want to capture the fact that sth fails and we fallback as well, i.e.
> 
> * if both sources succeed, we merge and trust MStar 100%
> * if one fails, we fallback to empty and still use the other successful one, but we won’t trust 100% and maybe log error to check
> 
> But the problem is same as what I explained in the exception retry comment, for no docs response, MStar sometimes gives valid xml with empty node, but it also sometimes give empty payload \(causing parsing exception\). And worst is it’s not consistent, empty payload can be retried and can give valid xml later. So we can’t be for sure.
> 
> ‌
> 
> I think for first cut, let’s go with this and we monitor more across the daily runs to see if we can improve further.
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Both sources success could trust fully, one failure should ideally flag fallback, but first cut monitored and retries expanded to both exception types.

**Evidence:** anon-1.jsonl:648 · comment 766402989 · PR 13460 · 2026-03-12

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/MstarInstrumentDocumentManager.scala`

**Explicit source context (pr_title):**

> [INV-4814] feat(instrument): MStar fund docs enhancements

## A1-0674 — Return empty only for legitimate no dividends; exhausted fallback throws 5xx

**Source stance:** requested-change

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala; operation: TT-7618 (dividend, marketdata): Added fallback api to fetch dividend detail from mstar; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Caller must retain ability to retry and track errors

**Source-preserving request, proposal, or question:**

> I think we should handle error properly so that we give chance to caller to retry if they want to?
> 
> * legit empty result → I would say it’s ok to just return empty list
> * any exception exhausting the fallback logic → Better to throw 5xx errors so that we can track
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:682 · comment 758589624 · PR 13402 · 2026-02-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> TT-7618 (dividend, marketdata): Added fallback api to fetch dividend detail from mstar

## A1-0676 — Use transform when no second Future call

**Source stance:** requested-change

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala; operation: TT-7618 (dividend, marketdata): Added fallback api to fetch dividend detail from mstar; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> transform is enough since we are not making another Future call

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:684 · comment 758605704 · PR 13402 · 2026-02-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> TT-7618 (dividend, marketdata): Added fallback api to fetch dividend detail from mstar

**Evidence:** anon-1.jsonl:684 · comment 758605704 · PR 13402 · 2026-02-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +      mstarInstrumentId = marketDataUploader.getMstarApiId(instrument)
> +
> +      historicalDistributionsEither = mstarApiService
> +        .getHistoricalDistributions(mstarInstrumentId, startDate)
> +        .transformWith {
> +          case Success(list) => Future.successful(Right(list))
> +          case Failure(ex)   =>
> +            logger.warn(s"Fetching Historical distributions from Mstar failed for instrument [$instrumentId]: ${ex.getMessage}")
> +            Future.successful(Left(ex))

## A1-0715 — Fetch standalone flag parallel with planMetrics since nonthrowing

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goaldetail/hk/HkExistingGoalDetailBehaviour.scala; operation: feat(bff, advisory): Add hasStandaloneOnlyFund flag to fundsmart goal detail behaviour and make funding source optional for fundsmart instrument list; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> And since we are not throwing, it’s possible to fetch this in parallel with the planMetrics

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:726 · comment 750004439 · PR 13347 · 2026-02-05

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goaldetail/hk/HkExistingGoalDetailBehaviour.scala`

**Explicit source context (pr_title):**

> feat(bff, advisory): Add hasStandaloneOnlyFund flag to fundsmart goal detail behaviour and make funding source optional for fundsmart instrument list

**Evidence:** anon-1.jsonl:726 · comment 750004439 · PR 13347 · 2026-02-05

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goaldetail/hk/HkExistingGoalDetailBehaviour.scala`

**Explicit source context (hunk):**

> +    val metricsFuture = fetchPlansPerformanceMetrics(plans = goal.plans, maybeGoalType = Some(goal.investmentGoalType))
> +    for {
> +      hasStandaloneOnlyFund <- hasStandaloneOnlyFundFuture
> +      metrics <- metricsFuture
> +    } yield {
> +      if (instrumentIds.size > 1 && hasStandaloneOnlyFund) {
> +        logger.error(s"Goal ${goal.goalId} is on multi-fund portfolio but contains standalone-only instrument")
> +      }
>        HkFundSmartGoalDetail(

## A1-0717 — Futures still sequential until assigned outside comprehension

**Source stance:** observed-defect

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goaldetail/hk/HkExistingGoalDetailBehaviour.scala; operation: feat(bff, advisory): Add hasStandaloneOnlyFund flag to fundsmart goal detail behaviour and make funding source optional for fundsmart instrument list; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> These are still sequential. Need to assign the fut outside

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:728 · comment 750017233 · PR 13347 · 2026-02-05

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goaldetail/hk/HkExistingGoalDetailBehaviour.scala`

**Explicit source context (pr_title):**

> feat(bff, advisory): Add hasStandaloneOnlyFund flag to fundsmart goal detail behaviour and make funding source optional for fundsmart instrument list

**Evidence:** anon-1.jsonl:728 · comment 750017233 · PR 13347 · 2026-02-05

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goaldetail/hk/HkExistingGoalDetailBehaviour.scala`

**Explicit source context (hunk):**

> -    fetchPlansPerformanceMetrics(plans = goal.plans, maybeGoalType = Some(goal.investmentGoalType)).map { metrics =>
> +    val instrumentIds = goal.plans.head.targetAssetAllocation.targetInstrumentWeights.keySet
> +    val hasStandaloneOnlyFundFuture = checkGoalContainsStandaloneInstruments(instrumentIds)
> +    val metricsFuture = fetchPlansPerformanceMetrics(plans = goal.plans, maybeGoalType = Some(goal.investmentGoalType))
> +    for {
> +      hasStandaloneOnlyFund <- hasStandaloneOnlyFundFuture
> +      metrics <- metricsFuture
> +    } yield {
> +      if (instrumentIds.size > 1 && hasStandaloneOnlyFund) {

## A1-0724 — Trigger monthly-data refresh only on changed stitch config

**Source stance:** suggestion

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/subscribers/InstrumentTopicSubscriber.scala; operation: Feat/INV-4918 stitch data fields; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Generic instrument updates are noisy with docs/projected returns

**Source-preserving request, proposal, or question:**

> This will be very noisy with the document sync / projected return updates etc. If we intend this to be called after stitch config update, ideally we want separate event for that.
> 
> However, in view of FIO project, and we don’t want to add events yet, maybe we can change on instrument svc side to check if stitch config was changed in the upsert/override request compared to existing data, and if so, instrument svc calls marketdata svc directly to refresh monthly changes.
> 
> IIRC, marketdata svc typically fetch instrument from entity again to confirm that indeed the instrument exists before performing any sync. So this would be safe.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Separate event ideal; FIO constraint suggests direct instrument-to-marketdata call, marketdata rechecks entity existence.

**Evidence:** anon-1.jsonl:735 · comment 736704260 · PR 12946 · 2026-01-12

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/subscribers/InstrumentTopicSubscriber.scala`

**Explicit source context (pr_title):**

> Feat/INV-4918 stitch data fields

## A1-0797 — Fold optional goalId into successful planId list or filtered plan IDs

**Source stance:** suggestion

**Context:**

> component: investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/RRTHelper.scala; operation: Feat/INV-5010 multi system rrt; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> ```scala
> goalId.fold(Future.successful(planId.map(List(_)))) {... Some(filteredPlanIds)... }
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:809 · comment 744912891 · PR 13145 · 2026-01-27

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/RRTHelper.scala`

**Explicit source context (pr_title):**

> Feat/INV-5010 multi system rrt

**Evidence:** anon-1.jsonl:809 · comment 744912891 · PR 13145 · 2026-01-27

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/RRTHelper.scala`

**Explicit source context (hunk):**

> +    goalId: Option[UUID],
> +    planId: Option[UUID],
> +    tradingAccountType: Option[TradingAccountType]
> +  ): Future[Seq[InvestmentRequestListAndInvestmentPlan]] = {
> +    for {
> +      maybePlanIdList <- goalId.fold(
> +        Future.successful(planId.map(s => Set(s.toString)))
> +      ) { goalId =>
> +        goalSvc.findGoalById(customerId = customerId, goalId = goalId, includePlans = true)

## A1-0803 — Run SIP check after advisoryClassification close to actual accept command

**Source stance:** requested-change

**Context:**

> component: rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/BaseServiceLogicImpl.scala; operation: [INV-5172] feat(rebalance): validate sip ack for rpc; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s call this after the `advisoryClassification` to ensure it’s as close as possible to the actual accept cmd

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:815 · comment 745790510 · PR 13218 · 2026-01-28

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-5172] feat(rebalance): validate sip ack for rpc

## A1-0807 — Wealth-admin retries impossible B2C and missing tenantId group lookups

**Source stance:** observed-defect

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala; operation: Feat/BB-3003 portfolio tenant api; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Repeated alerts, blind UUID parse and DB queries stem from poor response contract

**Source-preserving request, proposal, or question:**

> I take a look at the wealth-admin PR [
> […incidental material or intervening source omitted…]
> and I think the current approach will do more harm than adding values:
> 
> * Regardless of which portfolio the admin user selects, wealth-admin always fetch this endpoint. It does render the page even if this endpoint errors or return no data :white_check_mark:  \(after all we just want tenantName\)
> * However, we have 2 problems:
> 
>     * It has retry logic on any errors. This means if user selects B2C portfolio, the endpoint is called a few times \(but such attempts are futile\) and error logs/alerts will flood wealth-admin
>     * It expects tenantId to be returned, blindly parse it as string and convert to UUID. This means if user selects B2B group portfolio, the endpoint returns None, and once again errors are repeated due to retries. This is not to mention the unnecessary load on the db for the repeated queries \(it should be minimal in grand scheme of things, but why pay the cost for nothing\)
>     
> 
> ‌
> 
> I believe you will have to change the impl on your wealth-admin PR to address these problems anyway. Updating the response payload contract shouldn’t be too much additional effort. In fact, by having proper better contract, it would help the wealth-admin side make better code decision.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:819 · comment 746272105 · PR 12919 · 2026-01-29

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala`

> I take a look at the wealth-admin PR [

**Explicit source context (pr_title):**

> Feat/BB-3003 portfolio tenant api

**Evidence:** anon-1.jsonl:819 · comment 746272105 · PR 12919 · 2026-01-29

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala`

> and I think the current approach will do more harm than adding values:
> 
> * Regardless of which portfolio the admin user selects, wealth-admin always fetch this endpoint. It does render the page even if this endpoint errors or return no data :white_check_mark:  \(after all we just want tenantName\)
> * However, we have 2 problems:
> 
>     * It has retry logic on any errors. This means if user selects B2C portfolio, the endpoint is called a few times \(but such attempts are futile\) and error logs/alerts will flood wealth-admin
>     * It expects tenantId to be returned, blindly parse it as string and convert to UUID. This means if user selects B2B group portfolio, the endpoint returns None, and once again errors are repeated due to retries. This is not to mention the unnecessary load on the db for the repeated queries \(it should be minimal in grand scheme of things, but why pay the cost for nothing\)
>     
> 
> ‌
> 
> I believe you will have to change the impl on your wealth-admin PR to address these problems anyway. Updating the response payload contract shouldn’t be too much additional effort. In fact, by having proper better contract, it would help the wealth-admin side make better code decision.

## A1-0818 — Background SFTP metadata check returns successful Done without for-comprehension

**Source stance:** suggestion

**Context:**

> component: report-impl/src/main/scala/com/endowus/silver/report/impl/logic/service/impl/SgServiceLogicImpl.scala; operation: Resolve INV-5157: Run sftp metadata check process in the background; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Could have done without for comprehend
> 
> ```scala
> def ... {
>   logger.info(s"Started sftp metadata check against pdf files for yearMonth: $yearMonth")
>   sftpMetadataChecker.checkMetaDataAgainstPdfFiles(yearMonth)
>   Future.successful(Done)
> }
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Do not infer future completion awaited; source intentionally starts background process.

**Evidence:** anon-1.jsonl:830 · comment 745753292 · PR 13286 · 2026-01-28

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/logic/service/impl/SgServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> Resolve INV-5157: Run sftp metadata check process in the background

## A1-0821 — Use stream log or wireTap if losing some logs acceptable

**Source stance:** suggestion

**Context:**

> component: akka-abstraction-layer/src/main/scala/com/endowus/silver/projection/auto/AutoProjectionEventSourceProvider.scala; operation: [NE-363] introduce auto projection; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> better to use `log` or `wireTap` if we can afford to lose some of the logs

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:833 · comment 744466162 · PR 13219 · 2026-01-26

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/projection/auto/AutoProjectionEventSourceProvider.scala`

**Explicit source context (pr_title):**

> [NE-363] introduce auto projection

**Evidence:** anon-1.jsonl:833 · comment 744466162 · PR 13219 · 2026-01-26

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/projection/auto/AutoProjectionEventSourceProvider.scala`

**Explicit source context (hunk):**

> +      .wireTap(log(_))
> +      .mapConcat(identity)
> +      .map(mkEventEnvelope(_))
> +  }
> +
> +  private def mkEventEnvelope(r: EventTagRecord): EventEnvelope[Event] = {
> +    r.ordering.map(n =>
> +      EventEnvelope(
> +        offset        = Sequence(n),

## A1-0838 — Do not wrap synchronous Explore result in Future unnecessarily

**Source stance:** open-question

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/ExploreManager.scala; operation: Feat/BB-3178 make customer id optional explore api; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> No need to wrap these in Future?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:850 · comment 732342110 · PR 12961 · 2025-12-30

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/ExploreManager.scala`

**Explicit source context (pr_title):**

> Feat/BB-3178 make customer id optional explore api

**Evidence:** anon-1.jsonl:850 · comment 732342110 · PR 12961 · 2025-12-30

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/ExploreManager.scala`

**Explicit source context (hunk):**

> +    maybeLocale: Option[Locale],
> +    pageIdResolver: ExplorePersona => UUID
> +  ): Future[ExploreContentPageDto] = {
> +    val locale = maybeLocale.getOrElse(defaultLocaleByRegion(region))
> +    val persona = resolveAiPersona(tenantId)
> +    val pageId = pageIdResolver(persona)
> +    exploreDataCache.getCachedExploreContentPageDto(
> +      pageId = pageId,
> +      customerProfile = CustomerProfile(

## A1-0854 — Use Future.failed for standalone validation

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/ValidationHelpers.scala; operation: [INV-4869] feat(bff, advisory, instrument, portfolio): Add a flag for instruments which are marked as Standalone-only and add amount restriction in fund-smart invest flow summary; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> return Future.failed instead

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:866 · comment 736786194 · PR 13163 · 2026-01-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/ValidationHelpers.scala`

**Explicit source context (pr_title):**

> [INV-4869] feat(bff, advisory, instrument, portfolio): Add a flag for instruments which are marked as Standalone-only and add amount restriction in fund-smart invest flow summary

**Evidence:** anon-1.jsonl:866 · comment 736786194 · PR 13163 · 2026-01-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/ValidationHelpers.scala`

**Explicit source context (hunk):**

> }
>  
> +  def validateInstrumentMultiFundEligibility(instruments: Seq[InstrumentInfoDto]): Future[Done] = {
> +    if (instruments.size > 1 && instruments.exists(!InstrumentInfoDto.canBePartOfMultiFundPortfolio(_))) {
> +      Future.failed(BadRequest(s"Contain instruments cannot be part of multi-fund portfolio: ${instruments.map(_.id).mkString(",")}"))
> +    } else {
> +      Future.successful(Done)
> +    }
> +  }

## A1-0872 — Return instruments and weights from PortfolioSummary and BasePlanUpsertSummary

**Source stance:** suggestion

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/planupsert/sg/SgPlanUpsertSummaryBehaviour.scala; operation: [INV-4869] feat(bff, advisory, instrument, portfolio): Add a flag for instruments which are marked as Standalone-only and add amount restriction in fund-smart invest flow summary; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** generateSummary already fetches them

**Source-preserving request, proposal, or question:**

> Inside `generateSummary` we actually already have the instruments and weights already. I’d suggest to simply return them in `PortfolioSummary` and `BasePlanUpsertSummary`, instead of fetching again here

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:884 · comment 738994745 · PR 13163 · 2026-01-15

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/planupsert/sg/SgPlanUpsertSummaryBehaviour.scala`

**Explicit source context (pr_title):**

> [INV-4869] feat(bff, advisory, instrument, portfolio): Add a flag for instruments which are marked as Standalone-only and add amount restriction in fund-smart invest flow summary

## A1-0916 — Start independent goal-approval summary futures as vals then compose

**Source stance:** suggestion

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalmodify/sg/SgGoalModifyApprovalSummaryBehaviour.scala; operation: [BB-3126] feat(advisory)(bff): base goal modify commit; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Avoid nested calls and tuples while preserving dependent performance/validity timing

**Source-preserving request, proposal, or question:**

> We don’t really need all these nested calls and tuple right?
> 
> ```scala
> val currentSummaryFut = ...
> val displaySummaryFut = ...
> 
> val approvalCustomerDataFut = ...
> val approvalCreatorDataFut = ...
> val approvalSummaryFut = ...
> 
> val goalLevelFeesFut = ...
> 
> for {
>   currentSummary <- currentSummaryFut
>   displaySummary <- displaySummaryFut
> 
>   performanceMetricsSummaryFut = ...
>   approvalValidityFut = ...
> 
>   performanceMetricsSummary <- performanceMetricsSummaryFut
>   approvalValidity <- approvalValidityFut
> 
>   approvalCustomerData <- approvalCustomerDataFut
>   approvalCreatorData <- approvalCreatorDataFut
>   (manager, createdBy, blockedOn) <- approvalSummaryFut
> 
>   goalLevelFees <- goalLevelFeesFut
> } yield ...
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:929 · comment 733972169 · PR 12893 · 2026-01-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalmodify/sg/SgGoalModifyApprovalSummaryBehaviour.scala`

**Explicit source context (pr_title):**

> [BB-3126] feat(advisory)(bff): base goal modify commit

## A1-0929 — Compiler warnings found communication Future map versus flatMap bugs

**Source stance:** observed-defect

**Context:**

> component: communication-impl/src/main/scala/com/endowus/silver/communication/impl/v2/email/customer/CustomerEmailTopicProducer.scala; operation: Fatal compiler warnings; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Actual bugs spotted by the warnings for `communication` svc related to Future map vs flatmap

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:942 · comment 730844738 · PR 13132 · 2025-12-23

Source path: `communication-impl/src/main/scala/com/endowus/silver/communication/impl/v2/email/customer/CustomerEmailTopicProducer.scala`

**Explicit source context (pr_title):**

> Fatal compiler warnings

## A1-0943 — Compiler warning finds map/flatMap bug mixing DBIO and Future

**Source stance:** observed-defect

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentPortfolioSubscribersDataJdbcHandler.scala; operation: Fatal compiler warnings; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Another bug with map vs flatmap, and confusing DBIO vs Future

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:957 · comment 730846176 · PR 13132 · 2025-12-23

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentPortfolioSubscribersDataJdbcHandler.scala`

**Explicit source context (pr_title):**

> Fatal compiler warnings

**Evidence:** anon-1.jsonl:957 · comment 730846176 · PR 13132 · 2025-12-23

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentPortfolioSubscribersDataJdbcHandler.scala`

**Explicit source context (hunk):**

> -          case Some(_) => Future.unit
> -          case None => Future.failed(new Exception(s"Expected some record to be upserted for $TableName, but got None"))
> -        })
> -    )
> +    database.run(instrumentPortfolioSubscribersDataTable.insertOrUpdateAll(data)).flatMap {
> +      case Some(_) => Future.unit
> +      case None    => Future.failed(new Exception(s"Expected some record to be upserted for $TableName, but got None"))
> +    }
>    }

## A1-0960 — Check sgAckCheckConfig before tenant lookup

**Source stance:** requested-change

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/SgTradingRestrictionLogicImpl.scala; operation: [INV-5146] feat(compliance): Add test cases for EIP/SIP state change subscriber and use tenant service instead of tenant provider to support service endpoint web E2E tests; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Check `sgAckCheckConfig` first before calling tenant service

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:975 · comment 730825433 · PR 13124 · 2025-12-23

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/SgTradingRestrictionLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-5146] feat(compliance): Add test cases for EIP/SIP state change subscriber and use tenant service instead of tenant provider to support service endpoint web E2E tests

**Evidence:** anon-1.jsonl:975 · comment 730825433 · PR 13124 · 2025-12-23

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/SgTradingRestrictionLogicImpl.scala`

**Explicit source context (hunk):**

> -          }
> -        } else TradingRestrictionCheckResult(errors = Set.empty, capturedAcknowledgments = List.empty)
> -      } yield result
> -    } else Future.successful(TradingRestrictionCheckResult(errors = Set.empty, capturedAcknowledgments = List.empty))
> +    if (!sgAckCheckConfig.enabled) {
> +      Future.successful(TradingRestrictionCheckResult(errors = Set.empty, capturedAcknowledgments = List.empty))
> +    } else {
> +      tenantService.getClientByIdV2(customer.customerId).flatMap { tenant =>
> +        val isEndowusTenant = tenant.tenantId == TenantUtils.TenantIdEndowusSg

## A1-0961 — Return hasSipInstruments future directly without yield

**Source stance:** requested-change

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/SgTradingRestrictionLogicImpl.scala; operation: [INV-5014] bug(compliance): add sip pass check in sip ack required api; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Can just return `hasSipInstruments(instrumentIds)`, no need for yield
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:976 · comment 733054031 · PR 13150 · 2026-01-02

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/SgTradingRestrictionLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-5014] bug(compliance): add sip pass check in sip ack required api

**Evidence:** anon-1.jsonl:976 · comment 733054031 · PR 13150 · 2026-01-02

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/SgTradingRestrictionLogicImpl.scala`

**Explicit source context (hunk):**

> -    } else Future.successful(false)
> +    val sipStatus = SipHelper.calculateSipStatus(customer.sgCustomer)
> +    if (sgAckCheckConfig.enabled && !sipStatus.isSuitableForSip)
> +      hasSipInstruments(instrumentIds)
> +    else Future.successful(false)
>    }
>  
>    private def getTradingRestrictionResolversConfigByPlanId(

## A1-0971 — Fetch only after conditions match in all three flows

**Source stance:** requested-change

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/CustomerTopicSubscriber.scala; operation: [INV-5045] feat(compliance): implement state changes for sip ack; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Same for all 3 flows, only fetch if conditions are matched

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:986 · comment 724813760 · PR 13004 · 2025-12-09

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/CustomerTopicSubscriber.scala`

**Explicit source context (pr_title):**

> [INV-5045] feat(compliance): implement state changes for sip ack

**Evidence:** anon-1.jsonl:986 · comment 724813760 · PR 13004 · 2025-12-09

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/CustomerTopicSubscriber.scala`

**Explicit source context (hunk):**

> +  private def processFinancialDetailsUpdatedMsg(msg: FinancialDetailsUpdatedMsg): Future[Done] = {
> +    if (ackCheckConfig.enabled) {
> +      for {
> +        customer <- customerService.getCustomerV2(msg.customerId.get)
> +        _ <- processFinancialDetailsUpdatedMsgForSip(customer, msg)
> +      } yield Done
> +    } else {
> +      Future.successful(Done)
> +    }

## A1-0978 — Get needed planIds from PlanDto without investment/trading fetch

**Source stance:** requested-change

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/CustomerTopicSubscriber.scala; operation: [INV-5045] feat(compliance): implement state changes for sip ack; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> nits: Since we only need planIds here, it’s sufficient to check from planDto, no need extra calls to investment/trading

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:994 · comment 725136803 · PR 13004 · 2025-12-10

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/CustomerTopicSubscriber.scala`

**Explicit source context (pr_title):**

> [INV-5045] feat(compliance): implement state changes for sip ack

## A1-0988 — Use Sink.ignore

**Source stance:** requested-change

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/util/SipHelper.scala; operation: [INV-5045] feat(compliance): implement state changes for sip ack; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Can be `Sink.ignore`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1004 · comment 728903300 · PR 13004 · 2025-12-18

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/util/SipHelper.scala`

**Explicit source context (pr_title):**

> [INV-5045] feat(compliance): implement state changes for sip ack

**Evidence:** anon-1.jsonl:1004 · comment 728903300 · PR 13004 · 2025-12-18

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/util/SipHelper.scala`

**Explicit source context (hunk):**

> +            ackRemovalTime = ackRemovalTime,
> +          )
> +          refProvider.getSgPlanAcknowledgementManagerEntity(planId).ask(cmd)
> +        }
> +        .runWith(Sink.ignore)
> +    } yield Done
> +  }
>  
> -    SipStatus(

## A1-0989 — Use flatMap for SIP state-change future

**Source stance:** open-question

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/CustomerTopicSubscriber.scala; operation: [INV-5045] feat(compliance): implement state changes for sip ack; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> flatMap?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1005 · comment 728911185 · PR 13004 · 2025-12-18

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/CustomerTopicSubscriber.scala`

**Explicit source context (pr_title):**

> [INV-5045] feat(compliance): implement state changes for sip ack

**Evidence:** anon-1.jsonl:1005 · comment 728911185 · PR 13004 · 2025-12-18

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/CustomerTopicSubscriber.scala`

**Explicit source context (hunk):**

> +    if (ackCheckConfig.enabled) {
> +      for {
> +        customer <- customerService.getCustomerV2(msg.customerId.get)
> +        _ <- processFinancialDetailsUpdatedMsgForSip(customer, msg)
> +      } yield Done
> +    } else {
> +      Future.successful(Done)
> +    }
> +  }

## A1-1035 — Validate request before loading existing acknowledgement entity

**Source stance:** requested-change

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/SgTradingRestrictionLogicImpl.scala; operation: [INV-5014] feat(compliance): implement trading restriction for all the actions; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Validate this first before loading existing acks from entity

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1051 · comment 724178267 · PR 12948 · 2025-12-08

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/SgTradingRestrictionLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-5014] feat(compliance): implement trading restriction for all the actions

**Evidence:** anon-1.jsonl:1051 · comment 724178267 · PR 12948 · 2025-12-08

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/SgTradingRestrictionLogicImpl.scala`

**Explicit source context (hunk):**

> +    instrumentIdResolverContext: InstrumentIdResolverContext,
> +    customer: SgCustomerDto,
> +    planAcknowledgementResolverContext: PlanAcknowledgementResolverContext,
> +  ): Future[TradingRestrictionCheckResult] = {
> +    val sipStatus = calculateSipStatus(customer.sgCustomer)
> +    if (sipStatus.isSuitableForSip || !TenantUtils.isEndowusTenant(tenantProvider.get.id, localConfig)) {
> +      Future.successful(TradingRestrictionCheckResult(errors = Set.empty, capturedAcknowledgments = List.empty))
> +    } else {
> +      for {

## A1-1037 — IGT buy leg investOnce may rerun compliance without needed acknowledgements

**Source stance:** open-question

**Context:**

> component: trading-impl/src/main/scala/com/endowus/silver/trading/impl/utils/SgComplianceChecker.scala; operation: [INV-5014] feat(compliance): implement trading restriction for all the actions; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Review one-time and recurring sell-to-buy flow

**Source-preserving request, proposal, or question:**

> Double check how the e2e flow works. So trading svc performs this check at the beginning of sell leg, once redemption completes, trading svc would trigger buy leg - via investOnce I believe.
> 
> Will investment svc perform compliance check again at this point? If so, will it have the required acks? Same for recurring flow.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1053 · comment 724165451 · PR 12948 · 2025-12-08

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/utils/SgComplianceChecker.scala`

**Explicit source context (pr_title):**

> [INV-5014] feat(compliance): implement trading restriction for all the actions

## A1-1047 — Stream DB once and loop locales inside; otherwise mapAsync(1)

**Source stance:** requested-change

**Context:**

> component: instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/TranslationDataLogic.scala; operation: Resolve INV-4629: Translation data reconciliation logic; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** DB streaming connections precious; avoid concurrent locale streams

**Source-preserving request, proposal, or question:**

> DB connection is precious, let’s stream once and we can loop thru the locales instead?
> 
> If you still want to loop locales outside, then let’s mapAsync\(1\) only so that we don’t open concurrent streaming connections

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1064 · comment 675906191 · PR 12485 · 2025-08-28

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/TranslationDataLogic.scala`

**Explicit source context (pr_title):**

> Resolve INV-4629: Translation data reconciliation logic

## A1-1048 — Log individual recon invalid records and runFold count

**Source stance:** requested-change

**Context:**

> component: instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/TranslationDataLogic.scala; operation: Resolve INV-4629: Translation data reconciliation logic; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Do not collect full error collection

**Source-preserving request, proposal, or question:**

> No need to collect to full collections. We can log warn for each, and only runFold to total count - which can be used to log error outside

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1065 · comment 675907762 · PR 12485 · 2025-08-28

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/TranslationDataLogic.scala`

**Explicit source context (pr_title):**

> Resolve INV-4629: Translation data reconciliation logic

## A1-1053 — Stream templates before locales and validate tags without collecting

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/translation/AdvisoryDataTranslationLogic.scala; operation: Resolve INV-4629: Translation data reconciliation logic; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Current per-locale collection repeats all templates

**Source-preserving request, proposal, or question:**

> Actually here you’re collecting all templates multiple times \(x locales\), then check merged displayTags again.
> 
> Isn’t it better to stream template first, then loop thru the locales? Then you don’t need to collect the templates or their tags at all

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1070 · comment 680165620 · PR 12485 · 2025-09-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/translation/AdvisoryDataTranslationLogic.scala`

**Explicit source context (pr_title):**

> Resolve INV-4629: Translation data reconciliation logic

## A1-1057 — Normal-query reconciliation concurrency can be 2 or 4

**Source stance:** suggestion

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/translation/AdvisoryDataTranslationLogic.scala; operation: Resolve INV-4629: Translation data reconciliation logic; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> This one we can go with 2 or 4 I think

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1074 · comment 680151763 · PR 12485 · 2025-09-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/translation/AdvisoryDataTranslationLogic.scala`

**Explicit source context (pr_title):**

> Resolve INV-4629: Translation data reconciliation logic

**Evidence:** anon-1.jsonl:1074 · comment 680151763 · PR 12485 · 2025-09-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/translation/AdvisoryDataTranslationLogic.scala`

**Explicit source context (hunk):**

> +                templateErrors <- validateTemplate(t.template, locale)
> +                templateTagErrors <- validateAdvisoryTags(t.displayTags.toSet, locale)
> +              } yield (locale, templateErrors ++ templateTagErrors)
> +            }
> +            .wireTap(ValidationError.logErrors(logger, _))
> +            .runFold(ValidationError.ErrorCount.empty)(ValidationError.mergeErrorCount)
> +        }
> +        .runFold(ValidationError.ErrorCount.empty)({ case (errorCount, errorCountPerLocale) => errorCount + errorCountPerLocale })
> +    } yield {

## A1-1058 — Increase parallelism for another normal query

**Source stance:** requested-change

**Context:**

> component: instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/TranslationDataLogic.scala; operation: Resolve INV-4629: Translation data reconciliation logic; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Same here, we can increase parallelism here since it would be normal query only

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1075 · comment 680151950 · PR 12485 · 2025-09-08

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/TranslationDataLogic.scala`

**Explicit source context (pr_title):**

> Resolve INV-4629: Translation data reconciliation logic

**Evidence:** anon-1.jsonl:1075 · comment 680151950 · PR 12485 · 2025-09-08

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/TranslationDataLogic.scala`

**Explicit source context (hunk):**

> +          StreamSource(locales)
> +            .mapAsync(parallelism = 1) { locale =>
> +              translatableModel.validate(instrumentTranslationJdbcRepository.queryTranslations(_, locale)).map(it => (locale, it))
> +            }
> +            .wireTap(ValidationError.logErrors(logger, _))
> +            .runFold(ValidationError.ErrorCount.empty)(ValidationError.mergeErrorCount)
> +        }
> +        .runFold(ValidationError.ErrorCount.empty)({ case (errorCount, errorCountPerLocale) => errorCount + errorCountPerLocale })
> +

## A1-1064 — Validate tags per template and locale without collecting or exact deduplicated counts

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/translation/AdvisoryDataTranslationLogic.scala; operation: Resolve INV-4629: Translation data reconciliation logic; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Reconciliation count need not be exact

**Source-preserving request, proposal, or question:**

> It’s just recon. The count doesnt need to be exact. I think it’s cleaner to validate the tags per template \+ locale in the above log as well. No need to collect templates and toSet here.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1081 · comment 681454348 · PR 12485 · 2025-09-10

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/translation/AdvisoryDataTranslationLogic.scala`

**Explicit source context (pr_title):**

> Resolve INV-4629: Translation data reconciliation logic

## A1-1065 — Template parallelism 2 and locale 1 with current single locale

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/translation/AdvisoryDataTranslationLogic.scala; operation: Resolve INV-4629: Translation data reconciliation logic; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> 2 for templates and 1 for locale, since we “know” there’s only 1 supported locale as of now

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1082 · comment 681453051 · PR 12485 · 2025-09-10

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/translation/AdvisoryDataTranslationLogic.scala`

**Explicit source context (pr_title):**

> Resolve INV-4629: Translation data reconciliation logic

**Evidence:** anon-1.jsonl:1082 · comment 681453051 · PR 12485 · 2025-09-10

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/translation/AdvisoryDataTranslationLogic.scala`

**Explicit source context (hunk):**

> +                templateTagErrors <- validateAdvisoryTags(t.displayTags.toSet, locale)
> +              } yield (locale, templateErrors ++ templateTagErrors)
> +            }
> +            .wireTap(ValidationError.logErrors(logger, _))
> +            .runFold(ValidationError.ErrorCount.empty)(ValidationError.mergeErrorCount)
> +        }
> +        .runFold(ValidationError.ErrorCount.empty)({ case (errorCount, errorCountPerLocale) => errorCount + errorCountPerLocale })
> +    } yield {
> +      if (templateErrorCount.total > 0) {

## A1-1086 — Start readside and RRT in parallel; timeout RRT via firstCompletedOf

**Source stance:** requested-change

**Context:**

> component: akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableUtils.scala; operation: Initial EC POC Idea; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Underlying Futures cannot be cancelled

**Source-preserving request, proposal, or question:**

> Start `readSideLoader` and rrt in parallel
> 
> Wrap the rrt in timeout so that we can give up early \(we can’t cancel those futures tho\). See example of `firstCompletedOf` in akka health check

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1103 · comment 705806423 · PR 12767 · 2025-10-28

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableUtils.scala`

**Explicit source context (pr_title):**

> Initial EC POC Idea

## A1-1087 — Expected ask timeout is not error for RRT use case

**Source stance:** explanation

**Context:**

> component: goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala; operation: Initial EC POC Idea; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> We only expect asktimeout here which is not really an error for this use case

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1104 · comment 705807881 · PR 12767 · 2025-10-28

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> Initial EC POC Idea

**Evidence:** anon-1.jsonl:1104 · comment 705807881 · PR 12767 · 2025-10-28

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (hunk):**

> }
>      } yield ()
>  
> +  override def getCustomerGoalsByStatusUsingRRT(customerId: UUID, status: Option[Set[GoalStatus]]): Future[List[GoalDto]] =
> +    findCustomerGoalsViaRRT(customerId, status)
> +
>    override def getCustomerGoalsByStatus(customerId: UUID, status: Option[Set[GoalStatus]]): Future[List[GoalDto]] = {
> -    val goalsFut = for {
> +    for {

## A1-1092 — Always return at least readSideResults; only RRT should time out

**Source stance:** open-question

**Context:**

> component: akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala; operation: Initial EC POC Idea; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> We discussed that we would always return at least data from `readSideResults` right? Timeout handling is only if `rrtResults` takes too long?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1109 · comment 712510118 · PR 12767 · 2025-11-11

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala`

**Explicit source context (pr_title):**

> Initial EC POC Idea

## A1-1114 — Start timeout future first; race it against RRT plus merge then warn and refresh readside

**Source stance:** requested-change

**Context:**

> component: akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala; operation: Initial EC POC Idea; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Start `afterFut(throw)` first
> 
> ```scala
> res <- firstCompletedOf(afterFut, rrtFut + merge).recoverWith(log warn + refresh readside)
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1131 · comment 716207028 · PR 12767 · 2025-11-20

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala`

**Explicit source context (pr_title):**

> Initial EC POC Idea

## A1-1126 — No readSideFut val needed if fetched first

**Source stance:** requested-change

**Context:**

> component: akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala; operation: Initial EC POC Idea; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> nit: no need to assign `readSideFut` since we will fetch it first here

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:1143 · comment 717270447 · PR 12767 · 2025-11-24

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableHelper.scala`

**Explicit source context (pr_title):**

> Initial EC POC Idea

## A1-1136 — Use parallelism one for commands to same entity

**Source stance:** requested-change

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImpl.scala; operation: [INV-5017] feat(compliance): implement ack, warnings block and trading restriction apis; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Entity cannot execute commands in parallel

**Source-preserving request, proposal, or question:**

> Use parallelism = 1 here since we are accessing same entity, the cmd can’t be parallelized anyway

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:1153 · comment 724004432 · PR 13025 · 2025-12-08

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-5017] feat(compliance): implement ack, warnings block and trading restriction apis

## A1-1145 — Reuse fetched source goals for customer entrypoint and key names by goalId

**Source stance:** requested-change

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImpl.scala; operation: [INV-5017] feat(compliance): implement ack, warnings block and trading restriction apis; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Only target-goal entrypoint needs extra source-goal fetch

**Source-preserving request, proposal, or question:**

> Actually we only need to fetch source goalName if entrypoint is by \(target\) goalId. If entrypoint is by customerId, we would already fetch all live goals which would include the source goals as well?
> 
> And this goalName map can be keyed by goalId. It doesn’t need to repeat and keyed by planId?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1162 · comment 724042423 · PR 13025 · 2025-12-08

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-5017] feat(compliance): implement ack, warnings block and trading restriction apis

## A1-1160 — Throw inside map binding or use flatMap binding with Future.failed

**Source stance:** requested-change

**Context:**

> component: bff-impl/src/main/scala/com/endowus/silver/bff/impl/auth/guards/GuardsHandlerLogic.scala; operation: [INV-5022] feat(compliance): create api for financial situation ack; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> throw if using `=` \(map\), otherwise need to use `<-` \(flatmap\) if Future.failed

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1177 · comment 719254041 · PR 12917 · 2025-11-28

Source path: `bff-impl/src/main/scala/com/endowus/silver/bff/impl/auth/guards/GuardsHandlerLogic.scala`

**Explicit source context (pr_title):**

> [INV-5022] feat(compliance): create api for financial situation ack

**Evidence:** anon-1.jsonl:1177 · comment 719254041 · PR 12917 · 2025-11-28

Source path: `bff-impl/src/main/scala/com/endowus/silver/bff/impl/auth/guards/GuardsHandlerLogic.scala`

**Explicit source context (hunk):**

> }
>  
> +  def canActionForCustomerPlans(planIds: List[UUID], authorized: Authorized): Future[List[TracingContext.Tag[_]]] = {
> +    for {
> +      plans <- goalService.GoalApi.findPlansByIds(planIds.mkString(",")).withRetry(AlwaysRetryOnException, retrySettings)
> +      additionalContexts <- Source(plans)
> +        .mapAsync(parallelism = 4)(
> +          plan =>
> +            innerCanActionForCustomer(

## A1-1165 — Chain stream without materializing all acknowledgement inputs

**Source stance:** requested-change

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImpl.scala; operation: [INV-5022] feat(compliance): create api for financial situation ack; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> We can chain everything in same flow right? No need to materialize into memory

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1182 · comment 721183771 · PR 12917 · 2025-12-03

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-5022] feat(compliance): create api for financial situation ack

**Evidence:** anon-1.jsonl:1182 · comment 721183771 · PR 12917 · 2025-12-03

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +    val ack = PlanAcknowledgement.fromTradingRestrictionAcknowledgement(request.tradingAcknowledgement)
> +    Source(request.planIds)
> +      .grouped(MaximumBatchSize)
> +      .mapAsync(2) { planIdList =>
> +        goalService.findPlansByIds(planIdList.mkString(","))
> +      }
> +      .mapConcat(identity)
> +      .mapConcat { plan =>
> +        plan.recurringInvestmentSchedule.map { _ =>

## A1-1185 — findGoal sufficient for SIP warnings

**Source stance:** open-question

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImpl.scala; operation: [INV-5017] feat(bff, compliance): create warnings block apis; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Use findGoal is sufficient here?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1202 · comment 721230570 · PR 12915 · 2025-12-03

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-5017] feat(bff, compliance): create warnings block apis

**Evidence:** anon-1.jsonl:1202 · comment 721230570 · PR 12915 · 2025-12-03

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImpl.scala`

**Explicit source context (hunk):**

> override def queryGoalPlansTradingRestriction(goalId: UUID): Future[PlanTradingRestrictionResponse] = {
> -    // TODO: INV-5017 provide implementation
> -    Future.successful(PlanTradingRestrictionResponse(requireUnsuitableForSipAckRecurringSchedulePlans = List.empty))
> +    for {
> +      goal <- goalService.getGoalById(goalId)
> +      sourceGoalIds = getSourceGoalIds(Seq(goal))
> +      sourceGoalNamesMap <- getSourceGoalNamesMap(sourceGoalIds)
> +      detailedRecurringSchedules = getDetailedRecurringSchedules(Seq(goal), sourceGoalNamesMap)

## A1-1187 — Fetch plan details after confirming missing acknowledgements

**Source stance:** requested-change

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImpl.scala; operation: [INV-5017] feat(bff, compliance): create warnings block apis; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Ideally we only fetch the details after we confirm the acks are missing

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:1204 · comment 721228281 · PR 12915 · 2025-12-03

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-5017] feat(bff, compliance): create warnings block apis

## A1-1233 — Remove redundant map to Done

**Source stance:** open-question

**Context:**

> component: voucher-impl/src/main/scala/com/endowus/silver/voucher/impl/entities/voucher/processors/cassandra/VoucherEventProcessor.scala; operation: Feat/PG-1205 daily fee discount calculator; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Do we need this `.map(_ => Done)`?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1247 · comment 719922498 · PR 12828 · 2025-12-01

Source path: `voucher-impl/src/main/scala/com/endowus/silver/voucher/impl/entities/voucher/processors/cassandra/VoucherEventProcessor.scala`

**Explicit source context (pr_title):**

> Feat/PG-1205 daily fee discount calculator

**Evidence:** anon-1.jsonl:1247 · comment 719922498 · PR 12828 · 2025-12-01

Source path: `voucher-impl/src/main/scala/com/endowus/silver/voucher/impl/entities/voucher/processors/cassandra/VoucherEventProcessor.scala`

**Explicit source context (hunk):**

> -                  voucherIssuingReason = rewardedVoucher.issuingReason,
> -                  updatedBy = event.updatedBy,
> -                  updateReason = event.updateReason,
> +                .getVoucherWalletEntityRef(rewardedVoucher.receivingCustomer)
> +                .ask(
> +                  UpdateRewardedVoucherCmd(
> +                    _,
> +                    voucherType = voucherId.voucherType,
> +                    voucherCode = voucherId.code,

## A1-1271 — Check SIP instruments before calling compliance

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/ValidationHelpers.scala; operation: [INV-4994] feat(advisory, goal): Decouple logic between risk misalignment and financial situation and add SIP acknowledgement; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Call this first, only proceed to call compliance if contains SIP instruments

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1286 · comment 714640786 · PR 12924 · 2025-11-17

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/ValidationHelpers.scala`

**Explicit source context (pr_title):**

> [INV-4994] feat(advisory, goal): Decouple logic between risk misalignment and financial situation and add SIP acknowledgement

**Evidence:** anon-1.jsonl:1286 · comment 714640786 · PR 12924 · 2025-11-17

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/ValidationHelpers.scala`

**Explicit source context (hunk):**

> +    implicit executionContext: ExecutionContext
> +  ): Future[Boolean] = {
> +    for {
> +      hasValidAiStatus <- checkCustomerAIPIStatus(customerId)
> +      hasUnlistedSipInstrument = checkInstrumentsEipSipStatus(instruments)
> +      isSipAckApplicable <- if (!hasValidAiStatus && hasUnlistedSipInstrument) {
> +        isInvestmentPlanVsFinancialSituationMismatched(customerId)
> +      } else {
> +        Future.successful(false)

## A1-1295 — Consider internal repartitioned Kafka topic rather than sequential DB locking

**Source stance:** open-question

**Context:**

> component: timeseries-impl/src/main/scala/com/endowus/silver/timeseries/impl/logic/marketdata/impl/MarketDataLock.scala; operation: [NE-356] (timeseries) add locking support for marketdata processing; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Lock throw restarts subscription and rebalances all instances; DB lock loses graceful backpressure

**Source-preserving request, proposal, or question:**

> Inside we call lockOnce which will throw if unable to lock. We might change to some other flavour of locking method to enable retry etc, but eventually it will still throw. This will propagate the exception to the caller. If caller is akka projection / kafka subscriber, we would then restart the event by tag query / consumer subscription.
> 
> In your use case, it would be kafka consumer. And restarting a consumer in our current usage would cause a partition rebalance across all instances too.
> 
> Current approach \+ this new impl still restrict us to process everything sequentially. With db lock, we somewhat lost the graceful backpressure too. Have we considered using some sort of “internal” Kafka topic within timeseries that we rewrite the message’s partition key to ensure the messages in the sequence that we can control?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1310 · comment 712357504 · PR 12875 · 2025-11-11

Source path: `timeseries-impl/src/main/scala/com/endowus/silver/timeseries/impl/logic/marketdata/impl/MarketDataLock.scala`

**Explicit source context (pr_title):**

> [NE-356] (timeseries) add locking support for marketdata processing

## A1-1296 — Underlying failure releases lock and caller retry rejoins acquisition

**Source stance:** explanation

**Context:**

> component: timeseries-impl/src/main/scala/com/endowus/silver/timeseries/impl/logic/util/impl/DistributedLockLogicDbImpl.scala; operation: [NE-354] introduce database based locking mechanism; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Only pod crash can leave stuck lock, covered by stale-ack revoke

**Source-preserving request, proposal, or question:**

> OK this will ensure if the underlying logic fails, we will release the lock, and task will effectively rejoin the queue trying to acquire the lock again \(if it’s retried by caller\).
> 
> So the only time the lock is stuck is when the pod crashes after acquiring a lock -  which is taken care by force revoke due to stale acks \(see other comment\)

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1311 · comment 714591597 · PR 12874 · 2025-11-17

Source path: `timeseries-impl/src/main/scala/com/endowus/silver/timeseries/impl/logic/util/impl/DistributedLockLogicDbImpl.scala`

**Explicit source context (pr_title):**

> [NE-354] introduce database based locking mechanism

## A1-1297 — Force revoke uses deleteRequest matching stale lock

**Source stance:** requested-change

**Context:**

> component: timeseries-impl/src/main/scala/com/endowus/silver/timeseries/impl/logic/util/impl/DistributedLockLogicDbImpl.scala; operation: [NE-354] introduce database based locking mechanism; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** A revokes stale; C acquires; delayed B must not delete C

**Source-preserving request, proposal, or question:**

> Since this is force revoke, we want to use deleteRequest to ensure we only revoke the one with stale acks?
> 
> We might have race condition, \(even though unlikely\), we might run into situation that:
> 
> * task A and B both get barred and tried to revoke the lock with stale-ack satisfying the condition in `tryUnlockBasedOnExisting`
> * task A successfully revoke that lock
> * before task B manages to call the noop revoke, task C comes in and acquires the lock
> * task B now wrongfully revoke the lock of task C
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1312 · comment 714592873 · PR 12874 · 2025-11-17

Source path: `timeseries-impl/src/main/scala/com/endowus/silver/timeseries/impl/logic/util/impl/DistributedLockLogicDbImpl.scala`

**Explicit source context (pr_title):**

> [NE-354] introduce database based locking mechanism

## A1-1301 — MarketDataLock owns acquire retry separately from underlying releaseRetrySettings

**Source stance:** explanation

**Context:**

> component: timeseries-impl/src/main/scala/com/endowus/silver/timeseries/impl/logic/util/impl/DistributedLockLogicDbImpl.scala; operation: [NE-354] introduce database based locking mechanism; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Caller chooses retry to reduce Kafka rebalance; lock-once-or-fail semantics accepted

**Source-preserving request, proposal, or question:**

> Sorry I was not clear. I was commenting on the fact that this `releaseRetrySettings` is used for release-lock retry in this PR, AND for acquire-lock retry in `MarketDataLock` in [
> […incidental material or intervening source omitted…]
> ‌
> 
> I agree with the lock-once-or-fail semantics, and the caller should be the one decide to retry \(if at all\), e.g. in this use case, since the input source is kafka subscriber and we want to minimize the consumer rebalance. The retry of lockOnce is independent logic of `MarketDataLock`, and therefore we should create another retrySettings in `MarketDataLock` itself, and not reusing the underlying `releaseRetrySettings`
> 
> ‌
> 
> In hindsight, I should have commented this on the other PR, not this one :see_no_evil:

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1316 · comment 715085044 · PR 12874 · 2025-11-18

Source path: `timeseries-impl/src/main/scala/com/endowus/silver/timeseries/impl/logic/util/impl/DistributedLockLogicDbImpl.scala`

> Sorry I was not clear. I was commenting on the fact that this `releaseRetrySettings` is used for release-lock retry in this PR, AND for acquire-lock retry in `MarketDataLock` in [

**Explicit source context (pr_title):**

> [NE-354] introduce database based locking mechanism

**Evidence:** anon-1.jsonl:1316 · comment 715085044 · PR 12874 · 2025-11-18

Source path: `timeseries-impl/src/main/scala/com/endowus/silver/timeseries/impl/logic/util/impl/DistributedLockLogicDbImpl.scala`

> ‌
> 
> I agree with the lock-once-or-fail semantics, and the caller should be the one decide to retry \(if at all\), e.g. in this use case, since the input source is kafka subscriber and we want to minimize the consumer rebalance. The retry of lockOnce is independent logic of `MarketDataLock`, and therefore we should create another retrySettings in `MarketDataLock` itself, and not reusing the underlying `releaseRetrySettings`
> 
> ‌
> 
> In hindsight, I should have commented this on the other PR, not this one :see_no_evil:

## A1-1302 — Normal release must match original lock request

**Source stance:** observed-defect

**Context:**

> component: timeseries-impl/src/main/scala/com/endowus/silver/timeseries/impl/logic/util/impl/DistributedLockLogicDbImpl.scala; operation: [NE-354] introduce database based locking mechanism; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Starved A heartbeat lets B revoke/acquire; A completion must not delete B lock; Futures not cancelled

**Source-preserving request, proposal, or question:**

> Since we can’t cancel future, in some extreme scenario \(thread starvation \+ too aggressive `unlockDelay`\) \(or at least in theory\), we might run into a race condition such that:
> 
> * task A acquires the lock and goes on with its long running logic
> * thread starvation / CPU constraints causes the heartbeat ack to miss updates
> * aggressive `unlockDelay` enables other tasks to be able to take over the lock
> * task B revokes the lock of task A - this never cancels the currently running task A
> * task A finally completes, now attempts to release its lock
> 
> Here we call delete instead of deleteRequest, that means task A would remove the task B’s lock
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1317 · comment 715086775 · PR 12874 · 2025-11-18

Source path: `timeseries-impl/src/main/scala/com/endowus/silver/timeseries/impl/logic/util/impl/DistributedLockLogicDbImpl.scala`

**Explicit source context (pr_title):**

> [NE-354] introduce database based locking mechanism

## A1-1314 — Retry RPC task operation before giving up

**Source stance:** suggestion

**Context:**

> component: rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/processors/sg/RebalanceSuggestedWorkflowProjection.scala; operation: [BB-3055] feat(rebalance): adding RPC approvals; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Maybe we can retry before giving up?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1329 · comment 703477491 · PR 12776 · 2025-10-23

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/processors/sg/RebalanceSuggestedWorkflowProjection.scala`

**Explicit source context (pr_title):**

> [BB-3055] feat(rebalance): adding RPC approvals

**Evidence:** anon-1.jsonl:1329 · comment 703477491 · PR 12776 · 2025-10-23

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/processors/sg/RebalanceSuggestedWorkflowProjection.scala`

**Explicit source context (hunk):**

> +  }
> +
> +  private def createNewWorkflowTask(event: RebalanceRequestSuggestedEvt, clientData: ClientDtoV2): Future[Unit] = {
> +    val planId = event.planId
> +    val rebalanceRequestId = event.rebalanceRequest.rebalanceRequestId
> +    val createRequest = buildCreateWorkflowRequest(event, clientData)
> +
> +    val creationFuture = workflowEngineService.createTaskWithPendingApprovers(TaskType.RPC_REBALANCE, createRequest)
> +

## A1-1316 — Use Future.unit

**Source stance:** requested-change

**Context:**

> component: rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/processors/sg/RebalanceSuggestedWorkflowProjection.scala; operation: [BB-3055] feat(rebalance): adding RPC approvals; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Future.unit

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1331 · comment 703478058 · PR 12776 · 2025-10-23

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/processors/sg/RebalanceSuggestedWorkflowProjection.scala`

**Explicit source context (pr_title):**

> [BB-3055] feat(rebalance): adding RPC approvals

**Evidence:** anon-1.jsonl:1331 · comment 703478058 · PR 12776 · 2025-10-23

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/processors/sg/RebalanceSuggestedWorkflowProjection.scala`

**Explicit source context (hunk):**

> +    }
> +  }
> +
> +  private def createNewWorkflowTask(event: RebalanceRequestSuggestedEvt, clientData: ClientDtoV2): Future[Unit] = {
> +    val planId = event.planId
> +    val rebalanceRequestId = event.rebalanceRequest.rebalanceRequestId
> +    val createRequest = buildCreateWorkflowRequest(event, clientData)
> +
> +    val creationFuture = workflowEngineService.createTaskWithPendingApprovers(TaskType.RPC_REBALANCE, createRequest)

## A1-1317 — foreach starts background task cancellations without waiting; confirm intent

**Source stance:** open-question

**Context:**

> component: rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/processors/sg/RebalanceSuggestedWorkflowProjection.scala; operation: [BB-3055] feat(rebalance): adding RPC approvals; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> foreach here means we will cancel these in background, without waiting for response. Is it intended?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1332 · comment 703479510 · PR 12776 · 2025-10-23

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/processors/sg/RebalanceSuggestedWorkflowProjection.scala`

**Explicit source context (pr_title):**

> [BB-3055] feat(rebalance): adding RPC approvals

## A1-1331 — Use Source for bounded futures rather than start all at once

**Source stance:** requested-change

**Context:**

> component: rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/processors/sg/RebalanceSuggestedWorkflowProjection.scala; operation: [BB-3055] feat(rebalance): adding RPC approvals; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Make it a habit to not start all futures at once, and use Source instead

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1346 · comment 704289907 · PR 12776 · 2025-10-24

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/processors/sg/RebalanceSuggestedWorkflowProjection.scala`

**Explicit source context (pr_title):**

> [BB-3055] feat(rebalance): adding RPC approvals

**Evidence:** anon-1.jsonl:1346 · comment 704289907 · PR 12776 · 2025-10-24

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/processors/sg/RebalanceSuggestedWorkflowProjection.scala`

**Explicit source context (hunk):**

> +  }
> +
> +  private def buildCreateWorkflowRequest(event: RebalanceRequestSuggestedEvt, clientData: ClientDtoV2): CreateWorkflowRequest = {
> +    val rebalanceRequest = event.rebalanceRequest
> +    val references = Map(
> +      WorkflowReferenceKey.WorkflowId -> s"${TaskType.RPC_REBALANCE.toString}${event.planId}|${event.customerId}",
> +      WorkflowReferenceKey.PlanId -> event.planId.toString,
> +      WorkflowReferenceKey.RebalanceRequestId -> rebalanceRequest.rebalanceRequestId.toString,
> +      WorkflowReferenceKey.GoalId -> event.goalId.toString,

## A1-1339 — Use Future.unit in second RPC method

**Source stance:** requested-change

**Context:**

> component: rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/processors/sg/RebalanceSuggestedWorkflowProjection.scala; operation: [BB-3055] feat(rebalance): adding RPC approvals; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Future.unit

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1354 · comment 705355722 · PR 12776 · 2025-10-27

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/processors/sg/RebalanceSuggestedWorkflowProjection.scala`

**Explicit source context (pr_title):**

> [BB-3055] feat(rebalance): adding RPC approvals

**Evidence:** anon-1.jsonl:1354 · comment 705355722 · PR 12776 · 2025-10-27

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/processors/sg/RebalanceSuggestedWorkflowProjection.scala`

**Explicit source context (hunk):**

> +    tenantId: UUID
> +  )(selectFilters: ApprovalTaskSearchResponse => Boolean, parallelism: Int = 4): Future[Unit] = {
> +    workflowEngineService
> +      .searchApprovalsTasks(
> +        status = Some(ApprovalTaskStatus.PENDING),
> +        assigneeRole = None,
> +        taskTypes = Some(List(TaskType.RPC_REBALANCE)),
> +        tenantIds = Some(List(tenantId))
> +      )

## A1-1341 — Prepare manual retrigger endpoints because recovered failures bypass projection retries

**Source stance:** requested-change

**Context:**

> component: rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/processors/sg/RebalanceSuggestedWorkflowProjection.scala; operation: [BB-3055] feat(rebalance): adding RPC approvals; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Since we are recovering all failures in this class, the projection will not retry. Please prepare appropriate endpoints to support if such error happens in prod and we need to re-trigger them manually

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1356 · comment 705358108 · PR 12776 · 2025-10-27

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/processors/sg/RebalanceSuggestedWorkflowProjection.scala`

**Explicit source context (pr_title):**

> [BB-3055] feat(rebalance): adding RPC approvals

## A1-1362 — Use new redemption endpoint even with multiple calls per goal

**Source stance:** requested-change

**Context:**

> component: goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala; operation: [INV-4563] feat(bff, goal, redemption, trading): Add full redemption threshold endpoint; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Typically one plan max three; duplicate fee query accepted temporarily

**Source-preserving request, proposal, or question:**

> I think we should remove this whole thing together, and call the new endpoint and extract data from there.
> 
> For now, it’s ok to make multiple calls to redemption svc here, typically a goal has one plan only, and at most 3 plans. We will duplicate the customer fee query on redemption side, but should be not too bad.
> 
> We can consider adding another endpoint for goalId/customerId later

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Goal/customer bulk endpoint possible later.

**Evidence:** anon-1.jsonl:1378 · comment 700114933 · PR 12525 · 2025-10-15

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-4563] feat(bff, goal, redemption, trading): Add full redemption threshold endpoint

## A1-1364 — New endpoint already contains flag; extra getRedemptionPlanRedeemableStatusList unnecessary

**Source stance:** open-question

**Context:**

> component: trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/investmentTransfer/processors/InvestmentTransferEventProcessor.scala; operation: [INV-4563] feat(bff, goal, redemption, trading): Add full redemption threshold endpoint; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Do we need make this call `getRedemptionPlanRedeemableStatusList` just for this flag? Don’t we already have it in the response of the new endpoint?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1380 · comment 700116154 · PR 12525 · 2025-10-15

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/investmentTransfer/processors/InvestmentTransferEventProcessor.scala`

**Explicit source context (pr_title):**

> [INV-4563] feat(bff, goal, redemption, trading): Add full redemption threshold endpoint

## A1-1372 — Use getPlanRedeemableValue data instead of extra call; enrich if fields missing

**Source stance:** requested-change

**Context:**

> component: goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala; operation: [INV-4563] feat(bff, goal, redemption, trading): Add full redemption threshold endpoint; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Not fixing this? All data we need from this should be available in `getPlanRedeemableValue` already? And if anything is missing, we can consider adding them if needed

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1388 · comment 702903916 · PR 12525 · 2025-10-22

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-4563] feat(bff, goal, redemption, trading): Add full redemption threshold endpoint

## A1-1413 — mapFut already handles None as Future.successful(None)

**Source stance:** explanation

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgFundSmartInstrumentBuilder.scala; operation: Feat/INV-4904 display cpf sa public; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Yes, that’s taken care by mapFut
> 
> ```
> def mapFut[O](f: T => Future[O])(implicit ec: ExecutionContext): Future[Option[O]] = {
>   opt.map(f(_).map(Some(_))).getOrElse(Future.successful(None))
> }
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1429 · comment 698888564 · PR 12756 · 2025-10-13

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgFundSmartInstrumentBuilder.scala`

**Explicit source context (pr_title):**

> Feat/INV-4904 display cpf sa public

## A1-1422 — Bind newRecurring.resolvedFundingInstructions with equals not flatMap

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/planupsert/sg/SgPlanUpsertSubmitForApprovalBehaviour.scala; operation: [BB-2974][BB-2975]: Fix issue related to missing approval identifier; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> We should be using `resolvedFundingInstructions = newRecurring.resolvedFundingInstructions` instead \(note the `=` instead of `<-` as it’s not an Option\)

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1438 · comment 695001126 · PR 12684 · 2025-10-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/planupsert/sg/SgPlanUpsertSubmitForApprovalBehaviour.scala`

**Explicit source context (pr_title):**

> [BB-2974][BB-2975]: Fix issue related to missing approval identifier

## A1-1427 — Warn and rethrow trade-cancel command so projection retries

**Source stance:** requested-change

**Context:**

> component: trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/PlanTraderProjection.scala; operation: [INV-4562] feat(charge, redemption, trading): Automate fee handling; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Other remote calls may retry then error-log and give up

**Source-preserving request, proposal, or question:**

> Yes agree to log warn \+ rethrow for this cmd, and let projection stuck and retry. Here we are cancelling a trade that supposed to stuck in order generation.
> 
> And for other remote calls, we can retry and give up with error logs :thumbsup:

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1443 · comment 684464774 · PR 12500 · 2025-09-16

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/PlanTraderProjection.scala`

**Explicit source context (pr_title):**

> [INV-4562] feat(charge, redemption, trading): Automate fee handling

## A1-1449 — Decide throw versus retry-and-give-up to avoid projection block

**Source stance:** open-question

**Context:**

> component: trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/PlanTraderProjection.scala; operation: [INV-4562] feat(charge, redemption, trading): Automate fee handling; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Do we want to throw here? Or just give up after retry so that we don’t block projection

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1466 · comment 685509405 · PR 12500 · 2025-09-18

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/PlanTraderProjection.scala`

**Explicit source context (pr_title):**

> [INV-4562] feat(charge, redemption, trading): Automate fee handling

**Evidence:** anon-1.jsonl:1466 · comment 685509405 · PR 12500 · 2025-09-18

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/PlanTraderProjection.scala`

**Explicit source context (hunk):**

> +      trade <- refProvider.getPlanTraderEntityRef(planId).ask(GetTradeCmd(_, tradeId))
> +      _ <- refProvider
> +        .getPlanTraderEntityRef(planId)
> +        .ask(
> +          DeleteTradeRequestCmd(
> +            _,
> +            tradeId = tradeId,
> +            reason = reason,
> +            requestedBy = requestedBy,

## A1-1450 — Charge service throws so trading projection retries

**Source stance:** requested-change

**Context:**

> component: charge-impl/src/main/scala/com/endowus/silver/charge/impl/logic/service/impl/BaseServiceLogicImpl.scala; operation: [INV-4562] feat(charge, redemption, trading): Automate fee handling; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** No recovery needed without wrapping

**Source-preserving request, proposal, or question:**

> Hmmm but this is on charge svc side, so we should just throw so that the projection’s on trading svc can retry right?
> 
> If we don’t want to wrap, then there’s no need to recover here

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1467 · comment 685570762 · PR 12500 · 2025-09-18

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-4562] feat(charge, redemption, trading): Automate fee handling

## A1-1457 — Remove unnecessary fee-resolution recover

**Source stance:** requested-change

**Context:**

> component: trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/PlanTraderProjection.scala; operation: [INV-4562] feat(charge, redemption, trading): Automate fee handling; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Remove this recover

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1474 · comment 686091790 · PR 12500 · 2025-09-19

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/PlanTraderProjection.scala`

**Explicit source context (pr_title):**

> [INV-4562] feat(charge, redemption, trading): Automate fee handling

**Evidence:** anon-1.jsonl:1474 · comment 686091790 · PR 12500 · 2025-09-19

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/PlanTraderProjection.scala`

**Explicit source context (hunk):**

> +        .recover {
> +          case err =>
> +            logger.error(s"Failed to cancel corresponding fee charge request for trade id: $tradeId of plan id: $planId, please check", err)
> +        }
> +    } yield Done
> +  }
> +
>    private[processors] def handleAmountSellTradeTradeTerminalState(planId: UUID, trade: Trade): Future[Done] = {
>      // We don't check if the trade is amount-based because there was an edge case where an amount-based trade had no orders,

## A1-1460 — Remove no-op recover

**Source stance:** requested-change

**Context:**

> component: trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/PlanTraderProjection.scala; operation: [INV-4562] feat(charge, redemption, trading): Automate fee handling; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Remove this recover since we’re not doing anything inside

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1477 · comment 686090388 · PR 12500 · 2025-09-19

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/PlanTraderProjection.scala`

**Explicit source context (pr_title):**

> [INV-4562] feat(charge, redemption, trading): Automate fee handling

**Evidence:** anon-1.jsonl:1477 · comment 686090388 · PR 12500 · 2025-09-19

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/PlanTraderProjection.scala`

**Explicit source context (hunk):**

> +            redemptionRequestId = tradeId,
> +            requestedReason = Some(reason),
> +            requestedBy = Some(requestedBy),
> +            deletion = Some(true),
> +          )
> +        )
> +        .withRetry(shouldRetryOnException = AlwaysRetryOnException, settings = futureRetrySettings)
> +        .recover {
> +          case err =>

## A1-1479 — No Future needed for multi-funding expression

**Source stance:** open-question

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/FundSmartInstrumentBuilder.scala; operation: [INV-4832] feat(bff, advisory): Augment the current instrument list endpoint to support multiple funding sources; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Looks like we don’t need Future?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1496 · comment 691888788 · PR 12661 · 2025-10-01

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/FundSmartInstrumentBuilder.scala`

**Explicit source context (pr_title):**

> [INV-4832] feat(bff, advisory): Augment the current instrument list endpoint to support multiple funding sources

**Evidence:** anon-1.jsonl:1496 · comment 691888788 · PR 12661 · 2025-10-01

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/FundSmartInstrumentBuilder.scala`

**Explicit source context (hunk):**

> +              val mergedInstruments = (accInstruments ++ currInstruments).distinctBy(_.id)
> +
> +              val mergedInstrumentGoalTypes = (accInstrumentGoalTypes.keySet ++ currInstrumentGoalTypes.keySet).map { instrumentId =>
> +                instrumentId -> (accInstrumentGoalTypes.getOrElse(instrumentId, Set.empty) ++ currInstrumentGoalTypes.getOrElse(instrumentId, Set.empty))
> +              }.toMap
> +
> +              val mergedInvestorTypes = accInvestorTypes ++ currInvestorTypes
> +
> +              ((mergedInstruments, mergedInstrumentGoalTypes), mergedInvestorTypes)

## A1-1480 — runFold merge incrementally rather than collect all

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/FundSmartInstrumentBuilder.scala; operation: [INV-4832] feat(bff, advisory): Augment the current instrument list endpoint to support multiple funding sources; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> It’s better to runFold and merge as the element arrives instead of collecting them all and merge one shot

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1497 · comment 691889438 · PR 12661 · 2025-10-01

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/FundSmartInstrumentBuilder.scala`

**Explicit source context (pr_title):**

> [INV-4832] feat(bff, advisory): Augment the current instrument list endpoint to support multiple funding sources

## A1-1486 — Use runFold instead of async fold forcing successful Future

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/FundSmartInstrumentBuilder.scala; operation: [INV-4832] feat(bff, advisory): Augment the current instrument list endpoint to support multiple funding sources; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> We can just use runFold. No need to runFoldAsync and force return a future

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1503 · comment 691957917 · PR 12661 · 2025-10-01

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/FundSmartInstrumentBuilder.scala`

**Explicit source context (pr_title):**

> [INV-4832] feat(bff, advisory): Augment the current instrument list endpoint to support multiple funding sources

**Evidence:** anon-1.jsonl:1503 · comment 691957917 · PR 12661 · 2025-10-01

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/FundSmartInstrumentBuilder.scala`

**Explicit source context (hunk):**

> +              val mergedInstruments = (accInstruments ++ currInstruments).distinctBy(_.id)
> +
> +              val mergedInstrumentGoalTypes = (accInstrumentGoalTypes.keySet ++ currInstrumentGoalTypes.keySet).map { instrumentId =>
> +                instrumentId -> (accInstrumentGoalTypes.getOrElse(instrumentId, Set.empty) ++ currInstrumentGoalTypes.getOrElse(instrumentId, Set.empty))
> +              }.toMap
> +
> +              val mergedInvestorTypes = accInvestorTypes ++ currInvestorTypes
> +
> +              ((mergedInstruments, mergedInstrumentGoalTypes), mergedInvestorTypes)

## A1-1506 — Use getPortfolio(plan) when no productPortfolio needed

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goaldetail/sg/SgExistingGoalDetailBehaviour.scala; operation: [BB-2923] feat(advisory)(bff): adding plan upsert flow; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Just call `getPortfolio(plan)` if you don’t need productPortfolio?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1523 · comment 691977127 · PR 12652 · 2025-10-01

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goaldetail/sg/SgExistingGoalDetailBehaviour.scala`

**Explicit source context (pr_title):**

> [BB-2923] feat(advisory)(bff): adding plan upsert flow

**Evidence:** anon-1.jsonl:1523 · comment 691977127 · PR 12652 · 2025-10-01

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goaldetail/sg/SgExistingGoalDetailBehaviour.scala`

**Explicit source context (hunk):**

> override def faManagedAdvisedProduct(advisedProduct: productline.FAManagedAdvisedProductDto, goal: GoalDto): Future[ExistingGoalDetail] = {
> -    fetchPlansPerformanceMetrics(plans = goal.plans, maybeGoalType = None).map { metrics =>
> +    val plan = goal.plans.head
> +    for {
> +      portfolio <-  getPortfolio(plan)
> +      planPerformanceMetrics <- fetchPlansPerformanceMetrics(plans = goal.plans, maybeGoalType = None)
> +    } yield {
>        FAManagedAdvisedGoalDetail(
>          goal = goal,

## A1-1563 — Throw rather than Option because buildPortfolioOfferings already handles skip

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgAdvisedPortfolioOfferingsManager.scala; operation: [INV-4769] feat(advisory): create portfolio offerings api for income enhanced; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> IIRC, `buildPortfolioOfferings` already takes care of error handling and skip, so here we just need to throw. No need to return `Option[IncomeEnhancedPortfolio]`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1580 · comment 688144948 · PR 12618 · 2025-09-24

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgAdvisedPortfolioOfferingsManager.scala`

**Explicit source context (pr_title):**

> [INV-4769] feat(advisory): create portfolio offerings api for income enhanced

## A1-1626 — Bound workflow task futures with Akka stream

**Source stance:** requested-change

**Context:**

> component: bff-impl/src/main/scala/com/endowus/silver/bff/impl/logic/ApprovalsWorkflowServiceLogicImpl.scala; operation: [BB-2784] feat(bff)(workflow): exposing task by status api; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> This will start all futures at once. Better to use akka stream so that we can control the paralleism

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1642 · comment 682651015 · PR 12434 · 2025-09-12

Source path: `bff-impl/src/main/scala/com/endowus/silver/bff/impl/logic/ApprovalsWorkflowServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [BB-2784] feat(bff)(workflow): exposing task by status api

## A1-1634 — Workflow task search parallelism2 sufficient

**Source stance:** requested-change

**Context:**

> component: bff-impl/src/main/scala/com/endowus/silver/bff/impl/logic/ApprovalsWorkflowServiceLogicImpl.scala; operation: [BB-2784] feat(bff)(workflow): exposing task by status api; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> We don’t want to start everything at once. 2 should be sufficient here

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1650 · comment 684364974 · PR 12434 · 2025-09-16

Source path: `bff-impl/src/main/scala/com/endowus/silver/bff/impl/logic/ApprovalsWorkflowServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [BB-2784] feat(bff)(workflow): exposing task by status api

**Evidence:** anon-1.jsonl:1650 · comment 684364974 · PR 12434 · 2025-09-16

Source path: `bff-impl/src/main/scala/com/endowus/silver/bff/impl/logic/ApprovalsWorkflowServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +          advisoryServiceClient.SgAdvisoryApi
> +            .checkTasksApprovalValidity(TaskListApprovalValidityRequest(groupedTaskIds))
> +            .map(_.taskIdValidation)
> +        }
> +      }
> +      .runWith(Sink.fold(Map.empty[UUID, ApprovalValidity])(_ ++ _))
> +  }
> +
>    override def approveTask(taskId: UUID, taskType: TaskType, actionActor: ActionActor, payload: Option[JsValue]): Future[Unit] = {

## A1-1668 — Use earliestStartYM as endDate to avoid refetching recent data

**Source stance:** suggestion

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/managers/StitchMonthlyChangesManager.scala; operation: Feat/INV-4568 Automating stitched data computation; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> There’s a small optimization to pass earliestStartYM from collected here as endDate, so that we don’t load recent data again

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1685 · comment 681425386 · PR 12467 · 2025-09-10

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/managers/StitchMonthlyChangesManager.scala`

**Explicit source context (pr_title):**

> Feat/INV-4568 Automating stitched data computation

## A1-1672 — Pass start/end dates to limit stitch fetch response

**Source stance:** suggestion

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/managers/StitchMonthlyChangesManager.scala; operation: Feat/INV-4568 Automating stitched data computation; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Small optimization to pass startDate and endDate here to limit the response size

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1689 · comment 681428701 · PR 12467 · 2025-09-10

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/managers/StitchMonthlyChangesManager.scala`

**Explicit source context (pr_title):**

> Feat/INV-4568 Automating stitched data computation

**Evidence:** anon-1.jsonl:1689 · comment 681428701 · PR 12467 · 2025-09-10

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/managers/StitchMonthlyChangesManager.scala`

**Explicit source context (hunk):**

> +          .toList
> +      )
> +  }
> +
> +  private[managers] def getIndividualMonthlyReturn(
> +    fundInfo: MstarStitchSourceDto,
> +    l1Ter: BigDecimal,
> +    l1BaseCcy: CurrencyUnit,
> +    maybeEndYmExclusive: Option[YearMonth]

## A1-1679 — Use Akka stream to avoid starting all stitching Futures

**Source stance:** requested-change

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/managers/StitchMonthlyChangesManager.scala; operation: Feat/INV-4568 Automating stitched data computation; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Use akka stream so that we dont start all futures at once

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1696 · comment 681429315 · PR 12467 · 2025-09-10

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/managers/StitchMonthlyChangesManager.scala`

**Explicit source context (pr_title):**

> Feat/INV-4568 Automating stitched data computation

**Evidence:** anon-1.jsonl:1696 · comment 681429315 · PR 12467 · 2025-09-10

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/managers/StitchMonthlyChangesManager.scala`

**Explicit source context (hunk):**

> +    } else {
> +      if (request.allowMissingMonth) {
> +        logger.warn(
> +          s"Stitched data for [${request.instrumentSource.identifier}] is not continuous, missing: [$missingMonths], but allowMissingMonth is true, so returning with the missing months as is"
> +        )
> +        monthlyChanges
> +      } else {
> +        throw new MarketDataSvcException(
> +          s"Stitched data for [${request.instrumentSource.identifier}] is not continuous, missing: [$missingMonths]",

## A1-1700 — Set MStar enddate with startdate to fetch exactly one daily record

**Source stance:** suggestion

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; operation: [INV-4676] feat(marketdata): create api to get instrument daily price; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Btw, I think MStar supports setting `enddate` as well, in addition to `startdate` which we already use.
> 
> This way we can fetch exactly one record, and no need to filter below

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1718 · comment 682574332 · PR 12510 · 2025-09-12

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> [INV-4676] feat(marketdata): create api to get instrument daily price

## A1-1701 — Background reconciliation makes test flaky if return precedes completion

**Source stance:** open-question

**Context:**

> component: instrument-impl/src/test/scala/com/endowus/silver/instrument/impl/logic/service/TranslationDataLogicSpec.scala; operation: Resolve INV-4629: Add back filter stream from db; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Won’t this be flaky cuz we are running the recon in background and not waiting for it to complete before returing?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1719 · comment 684272522 · PR 12614 · 2025-09-16

Source path: `instrument-impl/src/test/scala/com/endowus/silver/instrument/impl/logic/service/TranslationDataLogicSpec.scala`

**Explicit source context (pr_title):**

> Resolve INV-4629: Add back filter stream from db

## A1-1727 — Cache instrument names even for no-longer-TAA instruments

**Source stance:** requested-change

**Context:**

> component: transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/HkEdgeLogicImpl.scala; operation: Feat/EN-4769 hk activity migration; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Avoid unconditional remote call though getInstrumentV2ByIds reads readside

**Source-preserving request, proposal, or question:**

> Yes, we still need to show instrument name for those, even if they are no longer in the goal’s TAA
> 
> `getInstrumentV2ByIds` goes to readside, but regardless of what instrument svc does, transaction svc shouldn’t need to make the remote call always, especially if it only cares about instrument name

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1745 · comment 641384693 · PR 11889 · 2025-06-05

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/HkEdgeLogicImpl.scala`

**Explicit source context (pr_title):**

> Feat/EN-4769 hk activity migration

## A1-1730 — Test throws NotFound synchronously instead of Future.failed

**Source stance:** observed-defect

**Context:**

> component: fxwallet-impl/src/test/scala/com/endowus/silver/fxwallet/impl/logic/service/FxWalletConversionServiceImplSpec.scala; operation: [NE-337] remove lagom transport exception usages; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Expected production wrapper FxWalletSvcException should be verified, not changed to satisfy test

**Source-preserving request, proposal, or question:**

> I guess you’re changing the prod code to catch NotFound explicitly because of this test?
> 
> But looks like this test itself should be change, since it throws NotFound directly via thenThrow instead of Future.failed… since by right, it should have verified that the exception is the wrapped FxWalletSvcException?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1748 · comment 680175622 · PR 12555 · 2025-09-08

Source path: `fxwallet-impl/src/test/scala/com/endowus/silver/fxwallet/impl/logic/service/FxWalletConversionServiceImplSpec.scala`

**Explicit source context (pr_title):**

> [NE-337] remove lagom transport exception usages

## A1-1735 — Approach accepted if no extra lookup

**Source stance:** explanation

**Context:**

> component: goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/PlanRecurringTransferScheduleTable.scala; operation: [INV-4302] feat(advisory, goal, trading, projection): inter-goal transfer v2 base; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> It’s fine, as long as we don’t need to incur another lookup

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1753 · comment 639843340 · PR 11795 · 2025-06-02

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/PlanRecurringTransferScheduleTable.scala`

**Explicit source context (pr_title):**

> [INV-4302] feat(advisory, goal, trading, projection): inter-goal transfer v2 base

**Evidence:** anon-1.jsonl:1753 · comment 639843340 · PR 11795 · 2025-06-02

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/PlanRecurringTransferScheduleTable.scala`

**Explicit source context (hunk):**

> +    tag,
> +    Some(PlanRecurringTransferScheduleTable.SchemaName),
> +    PlanRecurringTransferScheduleTable.TableName
> +  ) {
> +  def customerId: Rep[UUID] = column[UUID]("customer_id")
> +  def transferScheduleId: Rep[UUID] = column[UUID]("transfer_schedule_id")
> +  def transferDirection: Rep[TransferDirection] = column[TransferDirection]("transfer_direction")
> +  def sourceGoalId: Rep[UUID] = column[UUID]("source_goal_id")
> +  def sourcePlanId: Rep[UUID] = column[UUID]("source_plan_id")

## A1-1817 — Delete charge rows in bounded batches within one stream

**Source stance:** requested-change

**Context:**

> component: charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/DailyFeeCalculationManager.scala; operation: [INV-4695] feat(charge): Charge MV & DailyFee tables; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Avoid whole-stream memory and concurrent streams; local short delete acceptable

**Source-preserving request, proposal, or question:**

> So we want to avoid collecting for whole stream and bloat the memory usage, hence I want to perform the deletion in batches within the same stream. We won’t open multiple concurrent streaming connection \+ the deletion should be short-lived & not dependent on other remote calls, this should be ok.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1837 · comment 674435397 · PR 12487 · 2025-08-26

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/DailyFeeCalculationManager.scala`

**Explicit source context (pr_title):**

> [INV-4695] feat(charge): Charge MV & DailyFee tables

## A1-1834 — Map redemption plan and throw instead of flatMap Future.unit

**Source stance:** requested-change

**Context:**

> component: redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/utils/ValidationHelper.scala; operation: [INV-4680] fix(redemption): add validation redemption requests with non bank transfers; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> `getRedemptionPlan(planId).map` and if \+ throw is sufficient, no need to flatMap and return Future.unit
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1854 · comment 671805044 · PR 12462 · 2025-08-19

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/utils/ValidationHelper.scala`

**Explicit source context (pr_title):**

> [INV-4680] fix(redemption): add validation redemption requests with non bank transfers

## A1-1842 — Use flatMap

**Source stance:** requested-change

**Context:**

> component: charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/FeeManagerEntity.scala; operation: TT-6674 Add plan-level option to consume cash first for fee charges and subscribe to updates from Goal service; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> flatMap

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1862 · comment 664088097 · PR 12352 · 2025-07-31

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/FeeManagerEntity.scala`

**Explicit source context (pr_title):**

> TT-6674 Add plan-level option to consume cash first for fee charges and subscribe to updates from Goal service

**Evidence:** anon-1.jsonl:1862 · comment 664088097 · PR 12352 · 2025-07-31

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/FeeManagerEntity.scala`

**Explicit source context (hunk):**

> +      log.info(s"FeeManagerEntity $entityId received ModifyConsumeAvailableCashFirstCmd but it has the same value, so ignoring...")
> +      return Effect.ack(cmd.replyTo)
> +    }
> +    val evt = FeePlanConsumeAvailableCashFirstModifiedEvt(
> +      previousConsumeAvailableCashFirst = profile.consumeAvailableCashFirst,
> +      newConsumeAvailableCashFirst = cmd.consumeAvailableCashFirst,
> +      modifiedAt = timeZoneHelper.now,
> +    )
> +

## A1-1869 — Latest-date query or DB join/stream instead of per-row lookup

**Source stance:** requested-change

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; operation: Feat/INV-4001 daily nav and performance; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Add a method to return latest date for given instrument? You can also join and stream from db directly, instead of streaming from one table, and lookup for each of them

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1889 · comment 632690060 · PR 11805 · 2025-05-14

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> Feat/INV-4001 daily nav and performance

## A1-1875 — InstrumentCache already batches; remove outer batching

**Source stance:** requested-change

**Context:**

> component: portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/logic/service/impl/ServiceLogicImpl.scala; operation: [INV-4190] feat(instrument, portfolio): remove instrument entity from portfolio; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> InstrumentCache already batches inside, so we can remove all these completely

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:1895 · comment 632775096 · PR 11812 · 2025-05-14

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-4190] feat(instrument, portfolio): remove instrument entity from portfolio

## A1-1877 — Return portfolio then build DTO outside; reuse validated instruments

**Source stance:** requested-change

**Context:**

> component: portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/logic/service/impl/ServiceLogicImpl.scala; operation: [INV-4190] feat(instrument, portfolio): remove instrument entity from portfolio; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Why do we need to return instruments here already? Just stick with portfolio, and construct DTO outside?
> 
> Also we shouldn’t need to lookup instruments again right? Should be the same set returned from `validateRequestedAllocationAndInstruments` above?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1897 · comment 632774376 · PR 11812 · 2025-05-14

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-4190] feat(instrument, portfolio): remove instrument entity from portfolio

## A1-1878 — streamAll directly from DB instead of memory-loaded stream

**Source stance:** requested-change

**Context:**

> component: portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/logic/service/impl/ServiceLogicImpl.scala; operation: [INV-4190] feat(instrument, portfolio): remove instrument entity from portfolio; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s add streamAll method so that we can stream directly from DB, instead of querying everything into memory then stream from memory

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1898 · comment 632778581 · PR 11812 · 2025-05-14

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-4190] feat(instrument, portfolio): remove instrument entity from portfolio

## A1-1880 — Approach still waits Future

**Source stance:** explanation

**Context:**

> component: portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/logic/service/impl/ServiceLogicImpl.scala; operation: [INV-4190] feat(instrument, portfolio): remove instrument entity from portfolio; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> This will still wait for the future

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:1900 · comment 632779076 · PR 11812 · 2025-05-14

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-4190] feat(instrument, portfolio): remove instrument entity from portfolio

## A1-1891 — Entity requests concurrency2 or4 rather than10

**Source stance:** requested-change

**Context:**

> component: portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/logic/service/impl/ServiceLogicImpl.scala; operation: [INV-4190] feat(instrument, portfolio): remove instrument entity from portfolio; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Endpoint not urgent

**Source-preserving request, proposal, or question:**

> 10 is too much when hitting entity. There’s no rush for this endpoint, doing 2 or 4 is more than enough

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1911 · comment 633503612 · PR 11812 · 2025-05-16

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-4190] feat(instrument, portfolio): remove instrument entity from portfolio

## A1-1903 — Prefer MStarId docs and fallback ISIN only on failure/empty

**Source stance:** suggestion

**Context:**

> component: instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/MstarInstrumentDocumentManager.scala; operation: [INV-4569] feat(instrument): add error handling; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Avoid double call always; RF funds likely fail ISIN

**Source-preserving request, proposal, or question:**

> Actually now that I look at it, I think using MStarId is still our preference. Only rare case that MStarId fails or doesnt return data, only then we fallback to using ISIN \(instead of double call always\). These RF funds would most likely fail if fetching using ISIN.
> 
> Maybe we just do this for now, and observe more
> 
> ```scala
> mstarHistoricalDocuments <- if (mstarId.idType == MstarApiIdType.ISIN) {
>   mstarApiService.getHistoricalDocuments(mstarId)
> } else {
>   mstarApiService.getHistoricalDocuments(mstarId)
>     .transformWith {
>       case Success(docs) if docs.documents.nonEmpty => Future.successful(docs)
>       case _ => mstarApiService.getHistoricalDocuments(MstarApiId(instrument.id, MstarApiIdType.ISIN))
>     }
> }
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Observe after first implementation.

**Evidence:** anon-1.jsonl:1923 · comment 669623831 · PR 12435 · 2025-08-13

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/MstarInstrumentDocumentManager.scala`

**Explicit source context (pr_title):**

> [INV-4569] feat(instrument): add error handling

## A1-1941 — succeed returns before inner future and leaks mock invocation into next test

**Source stance:** observed-defect

**Context:**

> component: customer-impl/src/test/scala/com/endowus/silver/customer/impl/customer/processor/SgCustomerCommunicationV2EventProcessorTest.scala; operation: [PG-172] feat(compliance)(customer): Fix flaky tests in SgCustomerCommunicationV2ProjectionTest and DpmStatusRepositoryImplTest; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> This `succeed` will make the test returns successfully, without waiting for the inner future.
> 
> When next test runs, it will count towards the total invocation on brokerService mock

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1962 · comment 627678447 · PR 11745 · 2025-05-02

Source path: `customer-impl/src/test/scala/com/endowus/silver/customer/impl/customer/processor/SgCustomerCommunicationV2EventProcessorTest.scala`

**Explicit source context (pr_title):**

> [PG-172] feat(compliance)(customer): Fix flaky tests in SgCustomerCommunicationV2ProjectionTest and DpmStatusRepositoryImplTest

## A1-1957 — Instrument cache already retries

**Source stance:** explanation

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/FundSmartInstrumentBuilder.scala; operation: Feat/INV-4479 IFL edge add allocation; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> It’s already retried in the cache

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1978 · comment 662953132 · PR 12322 · 2025-07-29

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/FundSmartInstrumentBuilder.scala`

**Explicit source context (pr_title):**

> Feat/INV-4479 IFL edge add allocation

**Evidence:** anon-1.jsonl:1978 · comment 662953132 · PR 12322 · 2025-07-29

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/FundSmartInstrumentBuilder.scala`

**Explicit source context (hunk):**

> +    instrumentHoldingCache
> +      .getCachedInstrumentHolding(instrumentId)
> +      .recoverWith {
> +        case ex =>
> +          logger.error(s"Unable to fetchInstrumentHolding for $instrumentId. No data will be displayed", ex)
> +          Future.successful(Option.empty)
> +      }
> +  }
> +

## A1-1964 — RestartSource.onFailuresWithBackoff does not emit failure

**Source stance:** explanation

**Context:**

> component: silver-commons/src/main/scala/com/endowus/silver/commons/kafka/TopicSubscriber.scala; operation: Feat/TT-5945 allow setting number of consumers per pod for topic subscriber; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> `RestartSource.onFailuresWithBackoff` wouldn’t fail tho

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:1985 · comment 626277411 · PR 11658 · 2025-04-29

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/kafka/TopicSubscriber.scala`

**Explicit source context (pr_title):**

> Feat/TT-5945 allow setting number of consumers per pod for topic subscriber

## A1-1965 — RestartSource completion means graceful stop, failure unexpected termination

**Source stance:** explanation

**Context:**

> component: silver-commons/src/main/scala/com/endowus/silver/commons/kafka/TopicSubscriber.scala; operation: Feat/TT-5945 allow setting number of consumers per pod for topic subscriber; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Never means subscriber started or failed-to-start

**Source-preserving request, proposal, or question:**

> `RestartSource.onFailuresWithBackoff` sets `maxRestarts = Int.MaxValue`, i.e. this future shouldn’t complete with a failure
> 
> ```
> * Wrap the given [[Source]] with a [[Source]] that will restart it when it fails using an exponential backoff.
> *
> * This [[Source]] will never emit a failure, since the failure of the wrapped [[Source]] is always handled by
> * restarting. The wrapped [[Source]] can be cancelled by cancelling this [[Source]].
> * When that happens, the wrapped [[Source]], if currently running will be cancelled, and it will not be restarted.
> * This can be triggered simply by the downstream cancelling, or externally by introducing a [[KillSwitch]] right
> * after this [[Source]] in the graph.
> *
> * This uses the same exponential backoff algorithm as [[akka.pattern.Backoff]].
> ```
> 
> ‌
> 
> But ok if we don’t trust akka, then these 2 log entries are a bit misleading
> 
> * On Success, it means that the kafka subscription has been gracefully stopped. This is either during graceful shutdown, or something really went wrong \(cuz we don’t really stop our kafka consumer for normal topic - only the TaskTopicSubscriber supports this\). Nevertheless, it surely doesn’t mean “the subscriber has started”
> * On Failure, then something unexpected went wrong with the `RestartSource`. But it also doesn’t mean “the subscriber failed to start”, it just means the subscription stream was terminated with \(potentially fatal\) error
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Unlimited restarts; cancellation/kill switch controls stop; TaskTopicSubscriber special case.

**Evidence:** anon-1.jsonl:1986 · comment 626763164 · PR 11658 · 2025-04-30

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/kafka/TopicSubscriber.scala`

**Explicit source context (pr_title):**

> Feat/TT-5945 allow setting number of consumers per pod for topic subscriber

## A1-1970 — Fetch approval task before portfolio creation

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/sg/SgGoalApprovedForCreationBehaviour.scala; operation: [BB-2814] feat(advisory): pre-generate goal id; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Avoid orphan on failure; full idempotency still needs more work

**Source-preserving request, proposal, or question:**

> Let’s fetch task first before creating portfolio, to avoid orphaned portfolio just in case this fails. We will need to do more to ensure it’s fully idempotent, but it should be ok for now
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1991 · comment 661720612 · PR 12319 · 2025-07-25

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/sg/SgGoalApprovedForCreationBehaviour.scala`

**Explicit source context (pr_title):**

> [BB-2814] feat(advisory): pre-generate goal id

## A1-1988 — Do query users need includePlans

**Source stance:** open-question

**Context:**

> component: goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala; operation: [BB-2591] feat: exposed new enpoint to fetch goal by customer id and goal name; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Do you need to includePlans for your query purpose?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:2009 · comment 661634536 · PR 12251 · 2025-07-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [BB-2591] feat: exposed new enpoint to fetch goal by customer id and goal name

**Evidence:** anon-1.jsonl:2009 · comment 661634536 · PR 12251 · 2025-07-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +  override def findGoalByCustomerIdAndGoalName(customerId: UUID, goalName: String): Future[GoalDto] = {
> +    for{
> +      maybeGoalData <- goalJdbcRepository.findGoalByCustomerIdAndGoalName(customerId, goalName)
> +      goalData = maybeGoalData.map(_.goal).getOrElse(throw NotFound(s"Can not find goal for given customerId $customerId and goalName $goalName"))
> +      goal <- appendPlanToGoal(includePlans = true)(goalData)
> +    } yield goal
> +  }
> +
>    override def findPlan(planId: UUID): Future[PlanDto] = {

## A1-2003 — Feed DB stream directly to Source

**Source stance:** requested-change

**Context:**

> component: rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/managers/PortfolioVersionUpgradeRebalanceRequestsGenerator.scala; operation: [INV-1946] feat(rebalance): remove taa entity; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s stream and feed it directly to below Source

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:2022 · comment 652298048 · PR 12157 · 2025-07-02

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/managers/PortfolioVersionUpgradeRebalanceRequestsGenerator.scala`

**Explicit source context (pr_title):**

> [INV-1946] feat(rebalance): remove taa entity

**Evidence:** anon-1.jsonl:2022 · comment 652298048 · PR 12157 · 2025-07-02

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/managers/PortfolioVersionUpgradeRebalanceRequestsGenerator.scala`

**Explicit source context (hunk):**

> -      )
> -
> -      (totalProcessed, successfulCount, skippedReasonBreakdown) <- Source(subscriberPlanIds)
> -        .mapAsync(2)(getRebalancePlanStateForSubscribingPlanId)
> +      (totalProcessed, successfulCount, skippedReasonBreakdown) <- rebalancePlanJdbcRepository
> +        .streamActivePlansByPortfolioVersion(portfolioId = portfolioId, effectiveDate = fromVersion)
> +        .mapAsync(2) { record =>
> +          getRebalancePlanStateForSubscribingPlanId(record.planId)
> +        }

## A1-2022 — Recover per instrument so one failed download does not stop next

**Source stance:** requested-change

**Context:**

> component: composition-impl/src/main/scala/com/endowus/silver/composition/impl/utils/MstarDataDownloader.scala; operation: [INV-3999] feat(composition): pull mstar data; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Either we log error and recover in this method, or do it in outer call, so that if one instrument fails, we can move on to next one

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2041 · comment 655820814 · PR 12004 · 2025-07-11

Source path: `composition-impl/src/main/scala/com/endowus/silver/composition/impl/utils/MstarDataDownloader.scala`

**Explicit source context (pr_title):**

> [INV-3999] feat(composition): pull mstar data

## A1-2052 — Do not refetch customer-level data for every goal

**Source stance:** open-question

**Context:**

> component: goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/GoalEdgeLogicImpl.scala; operation: Feat/EN-4720 additional fields goal overview api; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Why did we change to this API? Isn’t it wasteful to keep fetching at customer level for each goal?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:2072 · comment 618790961 · PR 11541 · 2025-04-11

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/GoalEdgeLogicImpl.scala`

**Explicit source context (pr_title):**

> Feat/EN-4720 additional fields goal overview api

**Evidence:** anon-1.jsonl:2072 · comment 618790961 · PR 11541 · 2025-04-11

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/GoalEdgeLogicImpl.scala`

**Explicit source context (hunk):**

> +        recommendedPortfolioChanges <- rebalanceService.getRecommendedPortfolioChangesForGoal(goalId)
> +        hasPendingRpc = recommendedPortfolioChanges.exists(_.status == RebalanceRequestStatus.REBALANCING_SUGGESTED_PENDING_ACCEPTANCE)
> +      } yield hasPendingRpc
>      }
>  
>      def fetchGoalDetails(goalId: UUID, displayCcy: CurrencyUnit): Future[(Option[ProductLine], GoalDto, List[PlanDto], Boolean, List[CurrencyUnit])] = {

## A1-2065 — Check isFullRedemption before portfolio lookup for mandatory rebate

**Source stance:** requested-change

**Context:**

> component: charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/SkipPlanFeeChargeHelper.scala; operation: [INV-4127] feat(charge): skip redemption fee charge when instrument have mandatory rebate fee; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Since this method is specific for `classifyMandatoryRebateFeeProfile`, maybe just check `isFullRedemption` upfront to save the portfolio call

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2085 · comment 614894981 · PR 11492 · 2025-04-01

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/SkipPlanFeeChargeHelper.scala`

**Explicit source context (pr_title):**

> [INV-4127] feat(charge): skip redemption fee charge when instrument have mandatory rebate fee

## A1-2085 — Skip allowedInstrumentsResponse when stopping recurring schedule

**Source stance:** suggestion

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/planupsert/sg/SgPlanUpsertApprovalActionBehaviour.scala; operation: [INV-4186] feat(bff, advisory, communication, gateway): Add API for downloading supporting documents for INVEST task type; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Also approval action behavior; next PR

**Source-preserving request, proposal, or question:**

> small one for next PR, let’s avoid fetching `allowedInstrumentsResponse` and its supporting data if not required when stopping recurring schedule. Same here and in the approval action behaviour

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2105 · comment 618145216 · PR 11570 · 2025-04-10

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/planupsert/sg/SgPlanUpsertApprovalActionBehaviour.scala`

**Explicit source context (pr_title):**

> [INV-4186] feat(bff, advisory, communication, gateway): Add API for downloading supporting documents for INVEST task type

## A1-2095 — Retry interplan simulation request

**Source stance:** requested-change

**Context:**

> component: trading-impl/src/main/scala/com/endowus/silver/trading/impl/logic/service/InterPlanInstrumentTransferService.scala; operation: [INV-4064] feat(trading): add isRebalanceTriggeredImmediately field to inter-plan simulation endpoint; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s add retry here too

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:2115 · comment 616369770 · PR 11563 · 2025-04-04

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/logic/service/InterPlanInstrumentTransferService.scala`

**Explicit source context (pr_title):**

> [INV-4064] feat(trading): add isRebalanceTriggeredImmediately field to inter-plan simulation endpoint

**Evidence:** anon-1.jsonl:2115 · comment 616369770 · PR 11563 · 2025-04-04

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/logic/service/InterPlanInstrumentTransferService.scala`

**Explicit source context (hunk):**

> +    !isAutoRebalanceBlacklisted && isAutoRebalanceEnabled && isThresholdBreached
> +  }
> +
> +  private def getPlanFromRebalanceSvc(planId: UUID): Future[PlanRebalanceData] = {
> +    rebalanceService.getRebalancePlan(planId).invoke().map { response =>
> +      response.rebalancePlan match {
> +        case Some(rebalancePlan) => PlanRebalanceData.fromRebalancePlan(rebalancePlan)
> +        case None => throw BadRequest(s"No rebalance plan found for $planId")
> +      }

## A1-2122 — Bound RF fee lookup via Akka stream instead of Future.traverse

**Source stance:** requested-change

**Context:**

> component: charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/SkipPlanFeeChargeHelper.scala; operation: [INV-3720] feat(advisory, charge): enable fee charge for rf corporate client holding non rf funds; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Use akka stream and control and parallelism. This Future.traverse will start all the futures at once I think

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2139 · comment 570868578 · PR 10434 · 2024-11-27

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/SkipPlanFeeChargeHelper.scala`

**Explicit source context (pr_title):**

> [INV-3720] feat(advisory, charge): enable fee charge for rf corporate client holding non rf funds

## A1-2126 — Fetch RF by distinct tradingAccountTypes rather than per DIY plan

**Source stance:** requested-change

**Context:**

> component: charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/SkipPlanFeeChargeHelper.scala; operation: [INV-3720] feat(advisory, charge): enable fee charge for rf corporate client holding non rf funds; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Exclusive funds small enough to retain in memory

**Source-preserving request, proposal, or question:**

> This would be too many duplicated calls. Let’s find all tradingAccountTypes from `diyPlanProfiles` and fetch separately. Will use more memory, but should be fine cuz we are keeping only the exclusive RF funds

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2143 · comment 573036512 · PR 10434 · 2024-12-03

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/SkipPlanFeeChargeHelper.scala`

**Explicit source context (pr_title):**

> [INV-3720] feat(advisory, charge): enable fee charge for rf corporate client holding non rf funds

## A1-2173 — Old filter and customer lookup may now unnecessary

**Source stance:** open-question

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/InstrumentsAndFiltersManager.scala; operation: [INV-4091] fix(bff, advisory): Endpoint to query instruments for given customer; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Do we still need this filter as well as the customer lookup call?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:2190 · comment 610648609 · PR 11426 · 2025-03-19

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/InstrumentsAndFiltersManager.scala`

**Explicit source context (pr_title):**

> [INV-4091] fix(bff, advisory): Endpoint to query instruments for given customer

**Evidence:** anon-1.jsonl:2190 · comment 610648609 · PR 11426 · 2025-03-19

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/InstrumentsAndFiltersManager.scala`

**Explicit source context (hunk):**

> +    } yield result
> +  }
> +
>    def getInstrumentsAndFiltersForTenantFa(
>      tenantId: UUID,
>      tradingAccountType: TradingAccountType,

## A1-2182 — recover sufficient without further fetch

**Source stance:** requested-change

**Context:**

> component: investment-impl/src/main/scala/com/endowus/silver/investment/impl/logic/service/impl/ServiceLogicImpl.scala; operation: [INV-4109] fix(investment): trigger cancel investment request endpoint.; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> `recover` is sufficient since we are not fetching anything more

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:2199 · comment 610733921 · PR 11420 · 2025-03-19

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-4109] fix(investment): trigger cancel investment request endpoint.

**Evidence:** anon-1.jsonl:2199 · comment 610733921 · PR 11420 · 2025-03-19

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +        .invoke()
> +        .map(trade => {
> +          Some(trade)
> +        })
> +        .recover {
> +          case ex: TradingSvcException if (ex.errorType == TradingSvcErrorType.TRADE_DOES_NOT_EXIST) =>
> +            None
> +          case ex =>
> +            throw new Exception(

## A1-2215 — Use readside getInstrumentV2ByIds for email name

**Source stance:** requested-change

**Context:**

> component: communication-api/src/main/scala/com/endowus/silver/communication/api/localization/TranslatableData.scala; operation: [INV-3870] feat(communication, goal, investment): Investment Comms - Investment setup for Cash (One-time, recurring); trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** headOption missing logs then falls back instrumentId; entity fetch unnecessary

**Source-preserving request, proposal, or question:**

> This `getInstrumentV2` will go to entity. I think it’s sufficient to use readside for this, via `getInstrumentV2ByIds`
> 
> We can take `headOption`, log error if no result and fallback to use just instrumentId

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2232 · comment 599922628 · PR 11073 · 2025-02-26

Source path: `communication-api/src/main/scala/com/endowus/silver/communication/api/localization/TranslatableData.scala`

**Explicit source context (pr_title):**

> [INV-3870] feat(communication, goal, investment): Investment Comms - Investment setup for Cash (One-time, recurring)

## A1-2244 — Chain email and platform-notification futures

**Source stance:** requested-change

**Context:**

> component: investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/BaseInvestmentCommunicationEventProcessor.scala; operation: [INV-3870] feat(communication, goal, investment): Investment Comms - Investment setup for Cash (One-time, recurring); trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Need to chain these 2 futures, `publishOneTimeInvestmentCreatedEmail` and `publishInvestmentRequestCreatedPlatformNotification`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2261 · comment 600482107 · PR 11073 · 2025-02-27

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/BaseInvestmentCommunicationEventProcessor.scala`

**Explicit source context (pr_title):**

> [INV-3870] feat(communication, goal, investment): Investment Comms - Investment setup for Cash (One-time, recurring)

## A1-2246 — No grouping needed; mapAsync directly

**Source stance:** requested-change

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; operation: [INV-4024] feat(marketdata): Remove unneeded call; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> No need to group anymore? Just straight away mapAsync here

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:2263 · comment 599970521 · PR 11245 · 2025-02-26

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> [INV-4024] feat(marketdata): Remove unneeded call

## A1-2251 — Run MStar docs sync in background

**Source stance:** suggestion

**Context:**

> component: instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentDataUpdateManagerV2.scala; operation: [INV-3507] feat(instrument): create api to sync mstar instrument documents; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s run this in background?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:2268 · comment 598665415 · PR 10854 · 2025-02-21

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentDataUpdateManagerV2.scala`

**Explicit source context (pr_title):**

> [INV-3507] feat(instrument): create api to sync mstar instrument documents

**Evidence:** anon-1.jsonl:2268 · comment 598665415 · PR 10854 · 2025-02-21

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentDataUpdateManagerV2.scala`

**Explicit source context (hunk):**

> +    }
> +
> +    activeInstrumentsSource
> +      .mapAsync(parallelism = 4)(processInstrument)
> +      .runWith(Sink.ignore)
> +  }
> +
> +  private def updateFundDocumentsWithNewDocuments(
> +    instrument: Instrument,

## A1-2252 — Reject AI-only doc for nonactive AI/PI; check instrument flag before customer fetch

**Source stance:** requested-change

**Context:**

> component: instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/impl/ServiceLogicImplV2.scala; operation: [INV-3507] feat(instrument): create api to sync mstar instrument documents; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Should throw if `instrumentIsAiOnly && !isActiveAiPiCustomer`?
> 
> Also let’s check  `instrumentIsAiOnly` before fetching customer, it’s wasteful

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2269 · comment 598664008 · PR 10854 · 2025-02-21

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/impl/ServiceLogicImplV2.scala`

**Explicit source context (pr_title):**

> [INV-3507] feat(instrument): create api to sync mstar instrument documents

## A1-2262 — Start document sync then return successful Done for background handler

**Source stance:** requested-change

**Context:**

> component: instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentDataUpdateManagerV2.scala; operation: [INV-3507] feat(instrument): create api to sync mstar instrument documents; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> You just need this
> 
> ```
> override def syncInstrumentMstarDocumentsHandler(request: SyncInstrumentMstarDocumentsRequest): Future[Done] = {
>   syncInstrumentMstarDocuments(request)
>   Future.successful(Done)
> }
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2279 · comment 599636244 · PR 10854 · 2025-02-25

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentDataUpdateManagerV2.scala`

**Explicit source context (pr_title):**

> [INV-3507] feat(instrument): create api to sync mstar instrument documents

## A1-2265 — No instrument fetch needed here

**Source stance:** requested-change

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; operation: Feat/INV-4024 move to kafka sync; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Didn’t need to fetch the instrument here

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:2282 · comment 599962626 · PR 11233 · 2025-02-26

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> Feat/INV-4024 move to kafka sync

## A1-2266 — Start stream chunk size200KB–500KB to reduce network trips

**Source stance:** suggestion

**Context:**

> component: document-impl/src/main/scala/com/endowus/silver/document/impl/logic/service/BaseServiceLogicImpl.scala; operation: fixes the endpoint to stream properly increases max size for bff; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Needs tuning, not universal final size

**Source-preserving request, proposal, or question:**

> Need some tuning but maybe we can try with 200KB-500KB as starter, otherwise it will incur lots of network trips

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2283 · comment 608980980 · PR 11397 · 2025-03-14

Source path: `document-impl/src/main/scala/com/endowus/silver/document/impl/logic/service/BaseServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> fixes the endpoint to stream properly increases max size for bff

## A1-2279 — Error-log instead of throw to avoid workflow retries

**Source stance:** suggestion

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/B2BNotificationManager.scala; operation: [INV-3765] feat(adviosry): create apis for b2b approval notifcations; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Maybe just log error instead? Otherwise workflow-engine side will retry

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:2296 · comment 595171731 · PR 11000 · 2025-02-11

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/B2BNotificationManager.scala`

**Explicit source context (pr_title):**

> [INV-3765] feat(adviosry): create apis for b2b approval notifcations

## A1-2331 — Recover centrally so transform returns T rather than Option[T]

**Source stance:** suggestion

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/helper/ExploreHelper.scala; operation: [INV-4452] feat(advisory): create model portfolio pages; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Is it better to catch all and recover from here, so that the `transform` can still return `T` instead of `Option[T]` ?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2348 · comment 652246468 · PR 12025 · 2025-07-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/helper/ExploreHelper.scala`

**Explicit source context (pr_title):**

> [INV-4452] feat(advisory): create model portfolio pages

## A1-2333 — Translation failures transient and retryable; recover policy inconsistent

**Source stance:** open-question

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/helper/ExploreHelper.scala; operation: [INV-4452] feat(advisory): create model portfolio pages; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> We don’t expect translation to fail right? If it does, it should be transient and ok to retry? I don’t see similar recover logic for `translateContentPayload`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2350 · comment 652244328 · PR 12025 · 2025-07-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/helper/ExploreHelper.scala`

**Explicit source context (pr_title):**

> [INV-4452] feat(advisory): create model portfolio pages

## A1-2334 — Central fetchAndTransform catches logs and returns None

**Source stance:** suggestion

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/helper/ExploreHelper.scala; operation: [INV-4452] feat(advisory): create model portfolio pages; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Pass page/error context; transformations stay nonoptional

**Source-preserving request, proposal, or question:**

> Same approach only, just that we change here, instead of every `transform`
> 
> Something like this
> 
> ```
>   private def fetchAndTransform[T](
>     id: UUID,
>     pageName: String,
>     customerProfile: CustomerProfile,
>     transform: (ExploreData, String, CustomerProfile) => Future[T]
>   ): Future[Option[T]] = {
>     exploreRepository
>       .findById(id)
>       .flatMap { data =>
>         transform(data, pageName, customerProfile)
>       }
>       .map(Some(_))
>       .recover {
>         case ex =>
>           logger.error("blah", ex)
>           None
>       }
>   }
> ```
> 
> ‌
> 
> Probably need to pass some string context for the error log, but otherwise it’s common handling for all

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2351 · comment 652277134 · PR 12025 · 2025-07-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/helper/ExploreHelper.scala`

**Explicit source context (pr_title):**

> [INV-4452] feat(advisory): create model portfolio pages

## A1-2347 — Increase rebate processing parallelism to avoid slowness

**Source stance:** requested-change

**Context:**

> component: rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/distro/DistributionCalculator.scala; operation: Resolve INV-3823: Changes to skip rebate distribution for b2b clients.; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> I think we can parallel more, otherwise this will get very slow

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:2362 · comment 595678678 · PR 11013 · 2025-02-12

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/distro/DistributionCalculator.scala`

**Explicit source context (pr_title):**

> Resolve INV-3823: Changes to skip rebate distribution for b2b clients.

**Evidence:** anon-1.jsonl:2362 · comment 595678678 · PR 11013 · 2025-02-12

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/distro/DistributionCalculator.scala`

**Explicit source context (hunk):**

> def weightPlansByMarketValueOverPeriod(fromDate: LocalDate, toDate: LocalDate): Flow[PlanMarketValue, Entitlement, NotUsed] = {
>      val rebateIntervalLengthInDays = fromDate.until(toDate, DAYS) + 1
>      Flow[PlanMarketValue]
> +      .mapAsync(parallelism = 4)(planMarketValue =>
> +        for {
> +          isCustomerEligible <- isCustomerEligibleForRebates(planMarketValue.customerId)
> +        } yield Option.when(isCustomerEligible)(planMarketValue)
> +      )

## A1-2349 — Try parallelism4; node4/8 CPU count uncertain

**Source stance:** suggestion

**Context:**

> component: rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/distro/DistributionCalculator.scala; operation: Resolve INV-3823: Changes to skip rebate distribution for b2b clients.; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Maybe 4. I can’t remember if our node has 4 or 8 cpu cores

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:2364 · comment 595699891 · PR 11013 · 2025-02-12

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/distro/DistributionCalculator.scala`

**Explicit source context (pr_title):**

> Resolve INV-3823: Changes to skip rebate distribution for b2b clients.

**Evidence:** anon-1.jsonl:2364 · comment 595699891 · PR 11013 · 2025-02-12

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/distro/DistributionCalculator.scala`

**Explicit source context (hunk):**

> def weightPlansByMarketValueOverPeriod(fromDate: LocalDate, toDate: LocalDate): Flow[PlanMarketValue, Entitlement, NotUsed] = {
>      val rebateIntervalLengthInDays = fromDate.until(toDate, DAYS) + 1
>      Flow[PlanMarketValue]
> +      .mapAsync(parallelism = 4)(planMarketValue =>
> +        for {
> +          isCustomerEligible <- isCustomerEligibleForRebates(planMarketValue.customerId)
> +        } yield Option.when(isCustomerEligible)(planMarketValue)
> +      )

## A1-2352 — Instrument-cache grouping parallelism2

**Source stance:** suggestion

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/cache/InstrumentCache.scala; operation: Resolve INV-3958: Group instrument id for populating instrument cache.; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> I think we can go 2

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:2367 · comment 595677604 · PR 11095 · 2025-02-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/cache/InstrumentCache.scala`

**Explicit source context (pr_title):**

> Resolve INV-3958: Group instrument id for populating instrument cache.

**Evidence:** anon-1.jsonl:2367 · comment 595677604 · PR 11095 · 2025-02-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/cache/InstrumentCache.scala`

**Explicit source context (hunk):**

> -        instrument.id -> instrument
> -      }.toMap)
> +    Source(instrumentIds.toList)
> +      .grouped(maximumBatchSize)
> +      .mapAsync(parallelism = 2) { batchedInstrumentIds =>
> +        instrumentService
> +          .getInstrumentV2ByIds(batchedInstrumentIds.mkString(","))
> +          .invoke()
> +      }

## A1-2365 — Only project nonempty goal when requested; filter empty monthlyResults

**Source stance:** suggestion

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalmodify/sg/SgGoalModifySummaryBehaviour.scala; operation: [INV-4487] fix(advisory): SG/HK hide fs modify goal summary projection if insufficient historical data; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> ```scala
> maybeProjection <- Option.whenOptFut(shouldShowProjection && !isEmptyGoal) {
>   ...
> }.map(_.filter(_.monthlyResults.nonEmpty))
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2380 · comment 651309169 · PR 12141 · 2025-06-30

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalmodify/sg/SgGoalModifySummaryBehaviour.scala`

**Explicit source context (pr_title):**

> [INV-4487] fix(advisory): SG/HK hide fs modify goal summary projection if insufficient historical data

## A1-2377 — Readside getInstrumentV2ByIds sufficient instead of entity

**Source stance:** requested-change

**Context:**

> component: communication-api/src/main/scala/com/endowus/silver/communication/api/localization/TranslatableData.scala; operation: [INV-4041] feat(communication, goal, investment): Address Invest comms issues; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Use `getInstrumentV2ByIds` \(like prev impl\) so that we don’t hit entity. Readside is sufficient for this

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2393 · comment 608477575 · PR 11278 · 2025-03-13

Source path: `communication-api/src/main/scala/com/endowus/silver/communication/api/localization/TranslatableData.scala`

**Explicit source context (pr_title):**

> [INV-4041] feat(communication, goal, investment): Address Invest comms issues

## A2-0070 — Review: Can I propose we move the logic around a little:

**Source stance:** suggestion

**Context:**

> PR 5423 (Refactor (compliance/investment): Refactor RestrictionError/RestrictionWarning to include categories.), no inline path; original row 70.

**Concern stated in the source:** HkComplianceChecker already centralizes compliance calls and retry handling; CAT2 recurring simulation with missing acknowledgement remains uncertain.

**Source-preserving request, proposal, or question:**

> Can I propose we move the logic around a little:
> 
> * HkComplianceChecker is the only class in `investment` svc that talks to `compliance`
> 
>     * We move the simulation API here, and return `ComplianceValidationResult`
>     * All the retry logic is already in place
>     
> * Extract utils logic to derive suitability vs risk violation and reuse for both reminder / failed schedule emails
> 
>     * This can be another class, or even in object HkComplianceChecker
>     
> 
> ‌
> 
> We might also need to check the compliance simulation logic if we handle the simulation for recurring investment on CAT2 however missing the ack correctly. I don’t remember we have implemented that logic.

**Conditions and limits:**

- The commenter explicitly does not remember whether the CAT2 missing-ack simulation exists; row 73 subsequently reports checking it and finding it absent.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:70 · comment 377383296 · PR 5423 · 2023-03-13

**Evidence:** anon-2.jsonl:70 · comment 377383296 · PR 5423 · 2023-03-13

**Explicit source context (pr_title):**

> Refactor (compliance/investment): Refactor RestrictionError/RestrictionWarning to include categories.

## A2-0081 — CreateFixedMaturityProductGoal: If small number of goals then it’s ok, but ideally we could use an async loading cache here \+ go to readside instead of entity

**Source stance:** suggestion

**Context:**

> PR 9462 (Resolve INV-3172: Amend script to create goals for fixed maturity product customers.), amend-scripts/src/main/scala/goal/CreateFixedMaturityProductGoal.scala; original row 81.

**Concern stated in the source:** Entity calls are acceptable for few goals; an async loading cache with readside lookup is preferable at larger volume.

**Source-preserving request, proposal, or question:**

> If small number of goals then it’s ok, but ideally we could use an async loading cache here \+ go to readside instead of entity

**Conditions and limits:**

- The comment explicitly permits the existing approach for a small number of goals.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:81 · comment 514391773 · PR 9462 · 2024-06-28

Source path: `amend-scripts/src/main/scala/goal/CreateFixedMaturityProductGoal.scala`

**Evidence:** anon-2.jsonl:81 · comment 514391773 · PR 9462 · 2024-06-28

Source path: `amend-scripts/src/main/scala/goal/CreateFixedMaturityProductGoal.scala`

**Explicit source context (pr_title):**

> Resolve INV-3172: Amend script to create goals for fixed maturity product customers.

## A2-0153 — InvestmentPlanEventProcessor: Log that we are ignoring this event, and return Future.successful\(Done\) instead

**Source stance:** requested-change

**Context:**

> PR 10896 ([INV-3426] feat(bff, advisory, goal, investment): Approval flow), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentPlanEventProcessor.scala; original row 153.

**Source-preserving request, proposal, or question:**

> Log that we are ignoring this event, and return Future.successful\(Done\) instead

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:153 · comment 601853588 · PR 10896 · 2025-03-04

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentPlanEventProcessor.scala`

**Evidence:** anon-2.jsonl:153 · comment 601853588 · PR 10896 · 2025-03-04

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentPlanEventProcessor.scala`

**Explicit source context (pr_title):**

> [INV-3426] feat(bff, advisory, goal, investment): Approval flow

## A2-0272 — SgCustomerDailyFeesCalculator: For potential extension, we can add `allowedPlanFeeInstructionOverride` to `PlanChargeContext`

**Source stance:** suggestion

**Context:**

> PR 10097 ([EN-3954] (charge) integrate fee instruction with context), charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/sg/SgCustomerDailyFeesCalculator.scala; original row 272.

**Concern stated in the source:** For potential extension, we can add `allowedPlanFeeInstructionOverride` to `PlanChargeContext`

* all existing products would have `allowedPlanFeeInstructionOverride` as false
* `FAManagedBespokePlanChargeContext` would have the fetched `feeInstructions` \(validated to be non empty?\) and `allowedPlanFeeInstructionOverride` as true
* potentially a future product that allows using plan fee instructions if set, otherwise use the default fee calculator

‌

`FeeInstructionHelper.getTotalFeeOnDate` should work with feeInstruction instead of context

**Source-preserving request, proposal, or question:**

> For potential extension, we can add `allowedPlanFeeInstructionOverride` to `PlanChargeContext`
> 
> * all existing products would have `allowedPlanFeeInstructionOverride` as false
> * `FAManagedBespokePlanChargeContext` would have the fetched `feeInstructions` \(validated to be non empty?\) and `allowedPlanFeeInstructionOverride` as true
> * potentially a future product that allows using plan fee instructions if set, otherwise use the default fee calculator
> 
> ‌
> 
> `FeeInstructionHelper.getTotalFeeOnDate` should work with feeInstruction instead of context

**Conditions and limits:**

- Existing products default allowedPlanFeeInstructionOverride=false; FAManagedBespokePlanChargeContext may set true with fetched feeInstructions. Nonempty validation is explicitly questioned.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:272 · comment 552090360 · PR 10097 · 2024-10-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/sg/SgCustomerDailyFeesCalculator.scala`

**Evidence:** anon-2.jsonl:272 · comment 552090360 · PR 10097 · 2024-10-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/sg/SgCustomerDailyFeesCalculator.scala`

**Explicit source context (pr_title):**

> [EN-3954] (charge) integrate fee instruction with context

## A2-0320 — MarketDataUploader: Let’s use `runWithReporting` which gives some utility around logging / allowing to capture individual error and move on instead of blocking the stream

**Source stance:** requested-change

**Context:**

> PR 10400 ([INV-3609] feat(marketdata, instrument): improve marketdata monthly changes reliability), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; original row 320.

**Concern stated in the source:** runWithReporting can capture a per-item error and continue the stream.

**Source-preserving request, proposal, or question:**

> Let’s use `runWithReporting` which gives some utility around logging / allowing to capture individual error and move on instead of blocking the stream

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:320 · comment 568223418 · PR 10400 · 2024-11-20

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Evidence:** anon-2.jsonl:320 · comment 568223418 · PR 10400 · 2024-11-20

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> [INV-3609] feat(marketdata, instrument): improve marketdata monthly changes reliability

## A2-0401 — BaseAdvisoryServiceE4s: Let’s structure the endpoints like this. I missed this in prev PR, but maybe add `tenant` segment is good idea

**Source stance:** suggestion

**Context:**

> PR 10183 ([INV-3558] feat(bff, advisory): Portfolio Builder Fund Details), advisory-api/src/main/scala/com/endowus/silver/advisory/api/BaseAdvisoryServiceE4s.scala; original row 401.

**Source-preserving request, proposal, or question:**

> Let’s structure the endpoints like this. I missed this in prev PR, but maybe add `tenant` segment is good idea
> 
> ```
> object BaseAdvisoryApi {
>   // /api/v2/advisory/edge/fund-smart/instruments/:instrumentId (existing endpoint, serving both authenticated customer and no auth)
>   // /api/v1/advisory/edge/instruments/:instrumentId (this PR, intended for no-auth only)
> }
> 
> object TenantAwareAdvisoryApi {
>   object TenantFaAwareAdvisoryApi {
>     // /api/v1/advisory/edge/tenant/fa/instruments (fund list PR)
>     // /api/v1/advisory/edge/tenant/fa/instruments/:instrumentId (this PR)
>   }
> 
>   object TenantCustomerAwareAdvisoryApi {
>     // /api/v1/advisory/edge/tenant/customer/instruments (future PR for add goal / modify goal)
>     // /api/v1/advisory/edge/tenant/customer/instruments/:instrumentId (this PR)
>   }
> }
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:401 · comment 562319746 · PR 10183 · 2024-11-07

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/BaseAdvisoryServiceE4s.scala`

**Evidence:** anon-2.jsonl:401 · comment 562319746 · PR 10183 · 2024-11-07

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/BaseAdvisoryServiceE4s.scala`

**Explicit source context (pr_title):**

> [INV-3558] feat(bff, advisory): Portfolio Builder Fund Details

## A2-0414 — BaseAdvisoryServiceE4s: Should we create another API object for all these tenant specific endpoints? Their logic should extract the tenant from tracing context, and use it for c...

**Source stance:** suggestion

**Context:**

> PR 10182 ([INV-3430] feat(bff, advisory): Portfolio Builder Fund List), advisory-api/src/main/scala/com/endowus/silver/advisory/api/BaseAdvisoryServiceE4s.scala; original row 414.

**Concern stated in the source:** Tenant-specific APIs can use tenant tracing context after BFF auth/RBAC; faId is unnecessary until any future FA-specific RF need.

**Source-preserving request, proposal, or question:**

> Should we create another API object for all these tenant specific endpoints? Their logic should extract the tenant from tracing context, and use it for corp profile lookup.
> 
> This means for now, we do not need to have `faId` in the query params. On BFF, it would be an authenticated proxy endpoints with appropriate RBAC resource. Once that passes, `advisory` just need to proceed with the tenantId.
> 
> In future, if we ever need to support fa specific RF, an optional `faId` can be added?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:414 · comment 558075298 · PR 10182 · 2024-10-28

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/BaseAdvisoryServiceE4s.scala`

**Evidence:** anon-2.jsonl:414 · comment 558075298 · PR 10182 · 2024-10-28

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/BaseAdvisoryServiceE4s.scala`

**Explicit source context (pr_title):**

> [INV-3430] feat(bff, advisory): Portfolio Builder Fund List

## A2-0424 — SgInstrumentFilterManager: Maybe we can structure this trait like this

**Source stance:** suggestion

**Context:**

> PR 10182 ([INV-3430] feat(bff, advisory): Portfolio Builder Fund List), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgInstrumentFilterManager.scala; original row 424.

**Source-preserving request, proposal, or question:**

> Maybe we can structure this trait like this
> 
> ```scala
> package com.endowus.silver.advisory.impl.managers
> 
> trait InstrumentsAndFiltersManager[R <: SilverRegion] extends FundSmartInstrumentBuilder[R] {
> 
>   def getInstrumentsAndFiltersForCustomer(
>     customerId: UUID,
>     tradingAccountType: TradingAccountType,
>     includeAlts: Option[Boolean],
>     maybeGoalId: Option[UUID],
>     locale: Option[Locale]
>   ): Future[FundSmartInstrumentsAndFiltersV3] = {
>     def getAllowedInstrumentsResponseFetcher(investorType: InvestorType): Seq[InstrumentInfoDto] => Future[AllowedInstrumentsResponse] =
>       withoutCorporateRulesInstruments =>
>         corporateProductRuleService.allowedInstrumentsBasedOnCorporateProfile(
>           customerId = customerId,
>           maybeTradingAccountType = Some(tradingAccountType),
>           maybeGoalType = None,
>           instruments = withoutCorporateRulesInstruments,
>           maybeInvestorType = Some(investorType),
>           maybeFromInstrumentIds = None
>       )
> 
>     for {
>       investorType <- getInvestorTypeFromTradingAccount(customerId, tradingAccountType)
>       result <- getInstrumentsAndFilters(
>         getAllowedInstrumentsResponseFetcher(investorType),
>         maybeCustomerId = Some(customerId),
>         tradingAccountType = tradingAccountType,
>         investorType = investorType,
>         includeAlts = includeAlts,
>         maybeGoalId = maybeGoalId,
>         locale = locale
>       )
>     } yield result
>   }
> 
>   def getInstrumentsAndFiltersForTenantFa(
>     tenantId: UUID,
>     tradingAccountType: TradingAccountType,
>     includeAlts: Option[Boolean],
>     locale: Option[Locale]
>   ): Future[FundSmartInstrumentsAndFiltersV3] = {
>     def getAllowedInstrumentsResponseFetcher(investorType: InvestorType): Seq[InstrumentInfoDto] => Future[AllowedInstrumentsResponse] =
>       withoutCorporateRulesInstruments =>
>         corporateProductRuleService.allowedInstrumentsBasedOnCorporateProfileForTenant(
>           tenantId = tenantId,
>           maybeTradingAccountType = Some(tradingAccountType),
>           maybeGoalType = None,
>           instruments = withoutCorporateRulesInstruments,
>           maybeInvestorType = Some(investorType),
>           maybeFromInstrumentIds = None
>       )
> 
>     for {
>       investorType <- getInvestorTypeFromTradingAccountForAiPi(tradingAccountType)
>       result <- getInstrumentsAndFilters(
>         getAllowedInstrumentsResponseFetcher(investorType),
>         maybeCustomerId = None,
>         tradingAccountType = tradingAccountType,
>         investorType = investorType,
>         includeAlts = includeAlts,
>         maybeGoalId = None,
>         locale = locale
>       )
>     } yield result
>   }
>   
>   private def getInstrumentsAndFilters(
>     allowedInstrumentsResponseFetcher: Seq[InstrumentInfoDto] => Future[AllowedInstrumentsResponse],
>     maybeCustomerId: Option[UUID],
>     tradingAccountType: TradingAccountType,
>     investorType: InvestorType,
>     includeAlts: Option[Boolean],
>     maybeGoalId: Option[UUID],
>     locale: Option[Locale]
>   ): Future[FundSmartInstrumentsAndFiltersV3] = {
>     for {
>       (instruments, instrumentGoalTypes) <- getInstrumentsWithGoalTypes(allowedInstrumentsResponseFetcher, tradingAccountType, investorType, includeAlts)
>       (instruments, allPossibleTagsMap) <- buildFundSmartInstrumentAndTagData(...)
>       ...
>     } yield FundSmartInstrumentsAndFiltersV3(instruments, filters)
>   }
>   
>   private def getInstrumentsWithGoalTypes(
>     allowedInstrumentsResponseFetcher: Seq[InstrumentInfoDto] => Future[AllowedInstrumentsResponse],
>     tradingAccountType: TradingAccountType,
>     investorType: InvestorType,
>     includeAlts: Option[Boolean]
>   ): Future[(Seq[InstrumentInfoDto], Map[String, Set[InvestmentGoalType]])] = {
>     for {
>       withoutCorporateRulesInstruments <- diyInstrumentsCache.getCachedDiyInstruments(investorType, tradingAccountToCcyMap(tradingAccountType))
>       allowedInstrumentsResponse <- allowedInstrumentsResponseFetcher(withoutCorporateRulesInstruments)
>       
>       ...
>     } yield (filteredInstruments, instrumentGoalTypes)
> }
> ```
> 
> ‌

**Conditions and limits:**

- The full proposed trait keeps separate Customer/TenantFa fetchers and a shared private implementation, including account-specific investor-type resolution and cached instrument filtering.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:424 · comment 561783487 · PR 10182 · 2024-11-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgInstrumentFilterManager.scala`

**Evidence:** anon-2.jsonl:424 · comment 561783487 · PR 10182 · 2024-11-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgInstrumentFilterManager.scala`

**Explicit source context (pr_title):**

> [INV-3430] feat(bff, advisory): Portfolio Builder Fund List

## A2-0441 — InvestorTypeFixForNonSgdInstrumentWithCpfAndSrs: better to use `Source(instrumentsToUpdate).mapAsync(...)` so that we can control the parallelism

**Source stance:** requested-change

**Context:**

> PR 9436 ([INV-3011] feat(instrument): fix wrong investor type mapping with instrument (cpf and srs)), amend-scripts/src/main/scala/instrument/InvestorTypeFixForNonSgdInstrumentWithCpfAndSrs.scala; original row 441.

**Concern stated in the source:** Source.mapAsync allows controlled parallelism.

**Source-preserving request, proposal, or question:**

> better to use `Source(instrumentsToUpdate).mapAsync(...)` so that we can control the parallelism

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:441 · comment 513369127 · PR 9436 · 2024-06-25

Source path: `amend-scripts/src/main/scala/instrument/InvestorTypeFixForNonSgdInstrumentWithCpfAndSrs.scala`

**Evidence:** anon-2.jsonl:441 · comment 513369127 · PR 9436 · 2024-06-25

Source path: `amend-scripts/src/main/scala/instrument/InvestorTypeFixForNonSgdInstrumentWithCpfAndSrs.scala`

**Explicit source context (pr_title):**

> [INV-3011] feat(instrument): fix wrong investor type mapping with instrument (cpf and srs)

## A2-0485 — package: I’m thinking if we want to create a case class for this instead, so we can add more fields if needed in future

**Source stance:** suggestion

**Context:**

> PR 10077 ([INV-3441] feat(composition): use instrument EndowusAssetClassType map to calculate taa and aaa), composition-api/src/main/scala/com/endowus/silver/composition/api/models/breakdown/package.scala; original row 485.

**Source-preserving request, proposal, or question:**

> I’m thinking if we want to create a case class for this instead, so we can add more fields if needed in future
> 
> ```
> // can be Map or List, depending our usage needs
> endowusAssetClassTypeBreakdowns: List[EndowusAssetClassTypeBreakdownDto]
> 
> case class EndowusAssetClassTypeBreakdownDto(
>   assetClassType: EndowusAssetClassType,
>   targetWeight: BigDecimal,
>   actualWeight: BigDecimal
> )
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:485 · comment 546348674 · PR 10077 · 2024-09-27

Source path: `composition-api/src/main/scala/com/endowus/silver/composition/api/models/breakdown/package.scala`

**Evidence:** anon-2.jsonl:485 · comment 546348674 · PR 10077 · 2024-09-27

Source path: `composition-api/src/main/scala/com/endowus/silver/composition/api/models/breakdown/package.scala`

**Explicit source context (pr_title):**

> [INV-3441] feat(composition): use instrument EndowusAssetClassType map to calculate taa and aaa

## A2-0525 — HkCustomerDailyFeesCalculator: But this calculator should not split by product like that. If you see SG, except for flat rate or single fund fundsmart, they all follow same meth...

**Source stance:** suggestion

**Context:**

> PR 10103 (Release/EN-3547 hk fee charge), charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/hk/HkCustomerDailyFeesCalculator.scala; original row 525.

**Concern stated in the source:** But this calculator should not split by product like that. If you see SG, except for flat rate or single fund fundsmart, they all follow same methodology. HK is no different, and in general we should be consistent in our charge approach.

The effective logic here is same, but the code suggests if we ever have another product in HK in future, they might charge differently - which they should not….

**Source-preserving request, proposal, or question:**

> But this calculator should not split by product like that. If you see SG, except for flat rate or single fund fundsmart, they all follow same methodology. HK is no different, and in general we should be consistent in our charge approach.
> 
> The effective logic here is same, but the code suggests if we ever have another product in HK in future, they might charge differently - which they should not….

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:525 · comment 547874642 · PR 10103 · 2024-10-03

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/hk/HkCustomerDailyFeesCalculator.scala`

**Evidence:** anon-2.jsonl:525 · comment 547874642 · PR 10103 · 2024-10-03

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/hk/HkCustomerDailyFeesCalculator.scala`

**Explicit source context (pr_title):**

> Release/EN-3547 hk fee charge

## A2-0544 — HkChargeCommunicationProjection: This logic actually exists in `InitiateFeeRedemptionCmdHandler`, it’s best we rely on sequence of events, rather than duplicating it again.

**Source stance:** suggestion

**Context:**

> PR 10103 (Release/EN-3547 hk fee charge), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/hk/HkChargeCommunicationProjection.scala; original row 544.

**Concern stated in the source:** This logic actually exists in `InitiateFeeRedemptionCmdHandler`, it’s best we rely on sequence of events, rather than duplicating it again.

The communication logic in fact can be region agnostic as well \(the same way `InitiateFeeRedemptionCmdHandler` doesn’t care about sg or hk\). We can simply use the `redemptionDetails` \(instead of using amount from `discountDetails`, and having to assume that there is no tax involved\)

```
event.feeChargeRequest.redemptionDetails match {
  case Some(redemptionDetails) =>
    redemptionDetails.redeemedAmount match {
      case Some(chargeAmount) =>
        ...communication logic goes here...
      case None =>
        logger.error("... <unexpected-please-check> ... ")
        Future.successful(Done)
    }
  case None =>
    // waived without vouchers
    Future.successful(Done)
}
```

‌

**Source-preserving request, proposal, or question:**

> This logic actually exists in `InitiateFeeRedemptionCmdHandler`, it’s best we rely on sequence of events, rather than duplicating it again.
> 
> The communication logic in fact can be region agnostic as well \(the same way `InitiateFeeRedemptionCmdHandler` doesn’t care about sg or hk\). We can simply use the `redemptionDetails` \(instead of using amount from `discountDetails`, and having to assume that there is no tax involved\)
> 
> ```
> event.feeChargeRequest.redemptionDetails match {
>   case Some(redemptionDetails) =>
>     redemptionDetails.redeemedAmount match {
>       case Some(chargeAmount) =>
>         ...communication logic goes here...
>       case None =>
>         logger.error("... <unexpected-please-check> ... ")
>         Future.successful(Done)
>     }
>   case None =>
>     // waived without vouchers
>     Future.successful(Done)
> }
> ```
> 
> ‌

**Conditions and limits:**

- Communication follows FeeChargeCompletedEvt redemptionDetails: Some redeemedAmount sends; missing redeemedAmount logs unexpected and returns Done; None redemptionDetails is waived without vouchers and returns Done.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:544 · comment 550155826 · PR 10103 · 2024-10-08

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/hk/HkChargeCommunicationProjection.scala`

**Evidence:** anon-2.jsonl:544 · comment 550155826 · PR 10103 · 2024-10-08

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/hk/HkChargeCommunicationProjection.scala`

**Explicit source context (pr_title):**

> Release/EN-3547 hk fee charge

## A2-0558 — DistributionCalculatorHelperHk: Can we retry \+ fallback to entity for this, just to be on safe side?

**Source stance:** suggestion

**Context:**

> PR 10121 (TT-5089 remove cache customer status for HK trailer rebate), rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/distro/DistributionCalculatorHelperHk.scala; original row 558.

**Concern stated in the source:** Can we retry \+ fallback to entity for this, just to be on safe side?

**Source-preserving request, proposal, or question:**

> Can we retry \+ fallback to entity for this, just to be on safe side?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:558 · comment 549741742 · PR 10121 · 2024-10-07

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/distro/DistributionCalculatorHelperHk.scala`

**Evidence:** anon-2.jsonl:558 · comment 549741742 · PR 10121 · 2024-10-07

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/distro/DistributionCalculatorHelperHk.scala`

**Explicit source context (pr_title):**

> TT-5089 remove cache customer status for HK trailer rebate

## A2-0581 — package: Existing GoalDto continue to serve the generic usage of BE services, and “edge” usage of FE. We might add new edge B2C\*Dto for FE in future, but for now, we only need ...

**Source stance:** explanation

**Context:**

> PR 10010 (Feat/INV-3472 b2b product line), goal-api/src/main/scala/com/endowus/silver/goal/api/models/goal/package.scala; original row 581.

**Concern stated in the source:** Existing GoalDto continue to serve the generic usage of BE services, and “edge” usage of FE. We might add new edge B2C\*Dto for FE in future, but for now, we only need B2B\*Dto

**Source-preserving request, proposal, or question:**

> Existing GoalDto continue to serve the generic usage of BE services, and “edge” usage of FE. We might add new edge B2C\*Dto for FE in future, but for now, we only need B2B\*Dto

**Conditions and limits:**

- Existing GoalDto remains generic BE/edge FE; only new B2B DTO is needed now, with B2C edge DTOs deferred.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:581 · comment 545903881 · PR 10010 · 2024-09-26

Source path: `goal-api/src/main/scala/com/endowus/silver/goal/api/models/goal/package.scala`

**Evidence:** anon-2.jsonl:581 · comment 545903881 · PR 10010 · 2024-09-26

Source path: `goal-api/src/main/scala/com/endowus/silver/goal/api/models/goal/package.scala`

**Explicit source context (pr_title):**

> Feat/INV-3472 b2b product line

## A2-0626 — AkkaHttpAuthRecipesTest: Which executionContext is this? We should probably use the one from AsyncWordSpec right?

**Source stance:** open-question

**Context:**

> PR 9891 (Feat/endpoints4s bff phase2), bff-impl/src/test/scala/com/endowus/silver/bff/impl/auth/AkkaHttpAuthRecipesTest.scala; original row 626.

**Concern stated in the source:** Which executionContext is this? We should probably use the one from AsyncWordSpec right?

**Source-preserving request, proposal, or question:**

> Which executionContext is this? We should probably use the one from AsyncWordSpec right?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:626 · comment 537782683 · PR 9891 · 2024-09-03

Source path: `bff-impl/src/test/scala/com/endowus/silver/bff/impl/auth/AkkaHttpAuthRecipesTest.scala`

**Evidence:** anon-2.jsonl:626 · comment 537782683 · PR 9891 · 2024-09-03

Source path: `bff-impl/src/test/scala/com/endowus/silver/bff/impl/auth/AkkaHttpAuthRecipesTest.scala`

**Explicit source context (pr_title):**

> Feat/endpoints4s bff phase2

## A2-0637 — package: I suppose this is already inside the `lazy val corePortfolioOfferingResponseSchema` so these supporting JsonSchema of Map type don’t need to be lazy anymore, but better...

**Source stance:** open-question

**Context:**

> PR 9877 (phase 1 changes), advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/package.scala; original row 637.

**Concern stated in the source:** I suppose this is already inside the `lazy val corePortfolioOfferingResponseSchema` so these supporting JsonSchema of Map type don’t need to be lazy anymore, but better be consistent \(all lazy or all not\)

**Source-preserving request, proposal, or question:**

> I suppose this is already inside the `lazy val corePortfolioOfferingResponseSchema` so these supporting JsonSchema of Map type don’t need to be lazy anymore, but better be consistent \(all lazy or all not\)

**Conditions and limits:**

- Consistency of lazy schema values is requested; row 638 offers nesting the map schema inside its outer lazy value as an alternative.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:637 · comment 537294504 · PR 9877 · 2024-09-02

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/package.scala`

**Evidence:** anon-2.jsonl:637 · comment 537294504 · PR 9877 · 2024-09-02

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/package.scala`

**Explicit source context (pr_title):**

> phase 1 changes

## A2-0638 — package: Also, maybe let’s make the `JsonSchema[Map[TradingAccountType, SubscriptionAmountRegulation]]` follow the same approach, move it to be val inside the outer lazy val sch...

**Source stance:** suggestion

**Context:**

> PR 9877 (phase 1 changes), advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/package.scala; original row 638.

**Concern stated in the source:** Also, maybe let’s make the `JsonSchema[Map[TradingAccountType, SubscriptionAmountRegulation]]` follow the same approach, move it to be val inside the outer lazy val schema? Then no need to extract another common trait

**Source-preserving request, proposal, or question:**

> Also, maybe let’s make the `JsonSchema[Map[TradingAccountType, SubscriptionAmountRegulation]]` follow the same approach, move it to be val inside the outer lazy val schema? Then no need to extract another common trait

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:638 · comment 537294651 · PR 9877 · 2024-09-02

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/package.scala`

**Evidence:** anon-2.jsonl:638 · comment 537294651 · PR 9877 · 2024-09-02

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/package.scala`

**Explicit source context (pr_title):**

> phase 1 changes

## A2-0649 — SgGoalModifySummaryBehaviour: Maybe lookup portfolio outside first? We need another lookup without tradingAccountType

**Source stance:** open-question

**Context:**

> PR 9715 ([INV-3238] feat(advisory): create apis for goal modify flow), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalmodify/sg/SgGoalModifySummaryBehaviour.scala; original row 649.

**Concern stated in the source:** Maybe lookup portfolio outside first? We need another lookup without tradingAccountType

```
def findProductPortfolio(advisoryTag: AdvisoryTag, riskTarget: ModelPortfolioRiskTarget): Future[Seq[ProductPortfolio]] = {
```

‌

Then we can reuse existing `mapPlansToPortfolioBasedOnTradingAccount` which will match these to plans by tradingAccount

**Source-preserving request, proposal, or question:**

> Maybe lookup portfolio outside first? We need another lookup without tradingAccountType
> 
> ```
> def findProductPortfolio(advisoryTag: AdvisoryTag, riskTarget: ModelPortfolioRiskTarget): Future[Seq[ProductPortfolio]] = {
> ```
> 
> ‌
> 
> Then we can reuse existing `mapPlansToPortfolioBasedOnTradingAccount` which will match these to plans by tradingAccount

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:649 · comment 531576292 · PR 9715 · 2024-08-16

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalmodify/sg/SgGoalModifySummaryBehaviour.scala`

**Evidence:** anon-2.jsonl:649 · comment 531576292 · PR 9715 · 2024-08-16

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalmodify/sg/SgGoalModifySummaryBehaviour.scala`

**Explicit source context (pr_title):**

> [INV-3238] feat(advisory): create apis for goal modify flow

## A2-0663 — ProductPortfolioRepository: Nit: can move a little closer to this method so that they stay in pair \(similar to those with stockRatio\)

**Source stance:** suggestion

**Context:**

> PR 9715 ([INV-3238] feat(advisory): create apis for goal modify flow), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/db/repository/ProductPortfolioRepository.scala; original row 663.

**Concern stated in the source:** Nit: can move a little closer to this method so that they stay in pair \(similar to those with stockRatio\)

Also I think can overload with same name `findProductPortfolio`

```
def findProductPortfolio(
    advisoryTag: AdvisoryTag,
    riskTarget: ModelPortfolioRiskTarget,
    tradingAccountType: TradingAccountType
  ): Future[ProductPortfolio]
```

‌

**Source-preserving request, proposal, or question:**

> Nit: can move a little closer to this method so that they stay in pair \(similar to those with stockRatio\)
> 
> Also I think can overload with same name `findProductPortfolio`
> 
> ```
> def findProductPortfolio(
>     advisoryTag: AdvisoryTag,
>     riskTarget: ModelPortfolioRiskTarget,
>     tradingAccountType: TradingAccountType
>   ): Future[ProductPortfolio]
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:663 · comment 532701036 · PR 9715 · 2024-08-20

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/db/repository/ProductPortfolioRepository.scala`

**Evidence:** anon-2.jsonl:663 · comment 532701036 · PR 9715 · 2024-08-20

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/db/repository/ProductPortfolioRepository.scala`

**Explicit source context (pr_title):**

> [INV-3238] feat(advisory): create apis for goal modify flow

## A2-0673 — GoalModifyBehaviourHelpers: throw if using map \(`_ = ...`\), or `Future.failed` if using flatmap \(`_ <- ...`\)

**Source stance:** explanation

**Context:**

> PR 9715 ([INV-3238] feat(advisory): create apis for goal modify flow), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/GoalModifyBehaviourHelpers.scala; original row 673.

**Concern stated in the source:** throw if using map \(`_ = ...`\), or `Future.failed` if using flatmap \(`_ <- ...`\)

**Source-preserving request, proposal, or question:**

> throw if using map \(`_ = ...`\), or `Future.failed` if using flatmap \(`_ <- ...`\)

**Conditions and limits:**

- Map branch uses throw with `_ = ...`; flatMap branch uses Future.failed with `_ <- ...`.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:673 · comment 535558264 · PR 9715 · 2024-08-27

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/GoalModifyBehaviourHelpers.scala`

**Evidence:** anon-2.jsonl:673 · comment 535558264 · PR 9715 · 2024-08-27

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/GoalModifyBehaviourHelpers.scala`

**Explicit source context (pr_title):**

> [INV-3238] feat(advisory): create apis for goal modify flow

## A2-0707 — InstrumentMarketDataEventProcessor: Let’s wait for Future

**Source stance:** suggestion

**Context:**

> PR 9603 (Feat/INV-3271 marketdata portfolio entity phase 1), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/processors/InstrumentMarketDataEventProcessor.scala; original row 707.

**Concern stated in the source:** Let’s wait for Future

**Source-preserving request, proposal, or question:**

> Let’s wait for Future

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:707 · comment 524605428 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/processors/InstrumentMarketDataEventProcessor.scala`

**Evidence:** anon-2.jsonl:707 · comment 524605428 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/processors/InstrumentMarketDataEventProcessor.scala`

**Explicit source context (pr_title):**

> Feat/INV-3271 marketdata portfolio entity phase 1

## A2-0739 — PortfolioMonthlyChangesHelper: ```

**Source stance:** suggestion

**Context:**

> PR 9603 (Feat/INV-3271 marketdata portfolio entity phase 1), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/helpers/PortfolioMonthlyChangesHelper.scala; original row 739.

**Source-preserving request, proposal, or question:**

> ```
> taa <- maybePortfolioMonthlyChangesData
>   .map(_.instrumentWeights)
>   .map(Future.successful)
>   .getOrElse(loadPortfolioTaa(portfolioId, effectiveDate))
> _ <- publishPortfolioMonthlyChangesGenerationTask(portfolioId, effectiveDate, marketDataCcy, taa)
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:739 · comment 531598842 · PR 9603 · 2024-08-16

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/helpers/PortfolioMonthlyChangesHelper.scala`

**Evidence:** anon-2.jsonl:739 · comment 531598842 · PR 9603 · 2024-08-16

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/helpers/PortfolioMonthlyChangesHelper.scala`

**Explicit source context (pr_title):**

> Feat/INV-3271 marketdata portfolio entity phase 1

## A2-0783 — SgRecommendedInvestmentManager: Best if we can refactor to avoid make unnecessary calls

**Source stance:** suggestion

**Context:**

> PR 9739 (Feat/EN-3683 sg create a new api to get recommended investment amount), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgRecommendedInvestmentManager.scala; original row 783.

**Concern stated in the source:** Best if we can refactor to avoid make unnecessary calls

```
lazy val tierLevelFut = getCustomerIncomeTierLevel(customerId)
lazy val myInfoFinancialDataFut = getMyInfoFinancialData(customerId)

tradingAccountType match {
  case TradingAccountType.SINGAPORE_SGD_CASH_ACCOUNT =>
    tierLevelFut.map { level =>
      deriveRecommendationFromIncomeTier(level, RecommendedRecurringMonthlyAmountSgdCashBasedOnIncomeLevelMap)
    }

  case TradingAccountType.SINGAPORE_CPF_OA_ACCOUNT =>
    for {
      myInfoFinancialData <- myInfoFinancialDataFut
      response <- deriveRecommendationFromMyInfo(myInfoFinancialData) match {
        case Some(recommendation) =>
          Future.successful(recommendation)
        case None =>
          tierLevelFut.map { level =>
            deriveRecommendationFromIncomeTier(level, RecommendedRecurringMonthlyAmountCpfBasedOnIncomeLevelMap)
          }
      }
    } yield response

  case _ =>
    Future.successful(RecommendedInvestmentDto.noRecommendation())
}
```

‌

No need to split the helper methods too fine, especially when they are not used in more than one place

* `getCustomerIncomeTierLevel` can do both customer lookup and perform mapping to TierLevel
* `getMyInfoFinancialData` can do myinfo lookup, if found then return, else only then do onboarding lookup and perform mapping

‌

**Source-preserving request, proposal, or question:**

> Best if we can refactor to avoid make unnecessary calls
> 
> ```
> lazy val tierLevelFut = getCustomerIncomeTierLevel(customerId)
> lazy val myInfoFinancialDataFut = getMyInfoFinancialData(customerId)
> 
> tradingAccountType match {
>   case TradingAccountType.SINGAPORE_SGD_CASH_ACCOUNT =>
>     tierLevelFut.map { level =>
>       deriveRecommendationFromIncomeTier(level, RecommendedRecurringMonthlyAmountSgdCashBasedOnIncomeLevelMap)
>     }
> 
>   case TradingAccountType.SINGAPORE_CPF_OA_ACCOUNT =>
>     for {
>       myInfoFinancialData <- myInfoFinancialDataFut
>       response <- deriveRecommendationFromMyInfo(myInfoFinancialData) match {
>         case Some(recommendation) =>
>           Future.successful(recommendation)
>         case None =>
>           tierLevelFut.map { level =>
>             deriveRecommendationFromIncomeTier(level, RecommendedRecurringMonthlyAmountCpfBasedOnIncomeLevelMap)
>           }
>       }
>     } yield response
> 
>   case _ =>
>     Future.successful(RecommendedInvestmentDto.noRecommendation())
> }
> ```
> 
> ‌
> 
> No need to split the helper methods too fine, especially when they are not used in more than one place
> 
> * `getCustomerIncomeTierLevel` can do both customer lookup and perform mapping to TierLevel
> * `getMyInfoFinancialData` can do myinfo lookup, if found then return, else only then do onboarding lookup and perform mapping
> 
> ‌

**Conditions and limits:**

- SGD uses only income-tier lookup; CPF tries MyInfo first, falling back to income tier only if needed; unsupported account returns noRecommendation. Customer/onboarding lookup should also be lazy.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:783 · comment 530404623 · PR 9739 · 2024-08-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgRecommendedInvestmentManager.scala`

**Evidence:** anon-2.jsonl:783 · comment 530404623 · PR 9739 · 2024-08-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgRecommendedInvestmentManager.scala`

**Explicit source context (pr_title):**

> Feat/EN-3683 sg create a new api to get recommended investment amount

## A2-0811 — TopicSubscriber: We should use `topicSubscriberSettings.parallelism` here?

**Source stance:** suggestion

**Context:**

> PR 9440 ([LAGOM-97] (timeseries) Lagom client removal for timeseries), silver-commons/src/main/scala/com/endowus/silver/commons/kafka/TopicSubscriber.scala; original row 811.

**Concern stated in the source:** We should use `topicSubscriberSettings.parallelism` here?

**Source-preserving request, proposal, or question:**

> We should use `topicSubscriberSettings.parallelism` here?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:811 · comment 516347874 · PR 9440 · 2024-07-02

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/kafka/TopicSubscriber.scala`

**Evidence:** anon-2.jsonl:811 · comment 516347874 · PR 9440 · 2024-07-02

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/kafka/TopicSubscriber.scala`

**Explicit source context (pr_title):**

> [LAGOM-97] (timeseries) Lagom client removal for timeseries

## A2-0814 — TopicSubscriber: In the TaskTopicSubscribers, these are used to retry processing individual message \(before dropping them\). Here you’re using as config to restart the subscrip...

**Source stance:** suggestion

**Context:**

> PR 9440 ([LAGOM-97] (timeseries) Lagom client removal for timeseries), silver-commons/src/main/scala/com/endowus/silver/commons/kafka/TopicSubscriber.scala; original row 814.

**Concern stated in the source:** In the TaskTopicSubscribers, these are used to retry processing individual message \(before dropping them\). Here you’re using as config to restart the subscription when it terminates unexpectedly. Maybe we should rename these fields a bit.

**Source-preserving request, proposal, or question:**

> In the TaskTopicSubscribers, these are used to retry processing individual message \(before dropping them\). Here you’re using as config to restart the subscription when it terminates unexpectedly. Maybe we should rename these fields a bit.

**Conditions and limits:**

- Retrying an individual task message before dropping it differs from restarting a terminated subscription; configuration names should distinguish them.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:814 · comment 516348152 · PR 9440 · 2024-07-02

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/kafka/TopicSubscriber.scala`

**Evidence:** anon-2.jsonl:814 · comment 516348152 · PR 9440 · 2024-07-02

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/kafka/TopicSubscriber.scala`

**Explicit source context (pr_title):**

> [LAGOM-97] (timeseries) Lagom client removal for timeseries

## A2-0816 — TopicSubscriber: [person] As discussed, it’s actually not safe to blindly increase `parallelism` here when consuming messages from same partition \(only safe for the task topic\).

**Source stance:** suggestion

**Context:**

> PR 9440 ([LAGOM-97] (timeseries) Lagom client removal for timeseries), silver-commons/src/main/scala/com/endowus/silver/commons/kafka/TopicSubscriber.scala; original row 816.

**Concern stated in the source:** [person] As discussed, it’s actually not safe to blindly increase `parallelism` here when consuming messages from same partition \(only safe for the task topic\).

Maybe we can be very opinionated about this:

* `TopicSubscriber` should force `parallelism = 1`
* And another flavor say TopicParallelSubscriber that support say parallel msg processing using the safeMapAsync

‌

**Source-preserving request, proposal, or question:**

> [person] As discussed, it’s actually not safe to blindly increase `parallelism` here when consuming messages from same partition \(only safe for the task topic\).
> 
> Maybe we can be very opinionated about this:
> 
> * `TopicSubscriber` should force `parallelism = 1`
> * And another flavor say TopicParallelSubscriber that support say parallel msg processing using the safeMapAsync
> 
> ‌

**Conditions and limits:**

- Normal same-partition topic delivery should force parallelism=1; only task-topic processing is described as safe to parallelize. Another TopicParallelSubscriber with safeMapAsync is proposed.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:816 · comment 516749511 · PR 9440 · 2024-07-03

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/kafka/TopicSubscriber.scala`

> As discussed, it’s actually not safe to blindly increase `parallelism` here when consuming messages from same partition \(only safe for the task topic\).
> 
> Maybe we can be very opinionated about this:
> 
> * `TopicSubscriber` should force `parallelism = 1`
> * And another flavor say TopicParallelSubscriber that support say parallel msg processing using the safeMapAsync
> 
> ‌

**Evidence:** anon-2.jsonl:816 · comment 516749511 · PR 9440 · 2024-07-03

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/kafka/TopicSubscriber.scala`

**Explicit source context (pr_title):**

> [LAGOM-97] (timeseries) Lagom client removal for timeseries

## A2-0821 — ProductPortfolioRepository: Maybe we can keep this method generic, but only handle for CoreEnhanced for now…

**Source stance:** suggestion

**Context:**

> PR 9605 ([INV-3236] feat(advisory): create advisory endpoints for goal create), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/db/repository/ProductPortfolioRepository.scala; original row 821.

**Concern stated in the source:** Maybe we can keep this method generic, but only handle for CoreEnhanced for now…

```
def findProductPortfolio(
  advisoryTag: AdvisoryTag,
  riskTarget: ModelPortfolioRiskTarget,
  tradingAccountType: TradingAccountType
): Future[ProductPortfolio] = {
  findAllActiveForAdvisoryTag(advisoryTag)
    .filter(p => filterForTradingAccountType(advisoryTag, tradingAccountType, p))
    .filter(p => filterForRiskTarget(advisoryTag, riskTarget, p))
    .runWith(Sink.headOption)
    .flatMap({
      case Some(productPortfolio) => Future.successful(productPortfolio)
      case None =>
        Future
          .failed(BadRequest(s"Unable to find $advisoryTag portfolio for trading account $tradingAccountType with risk target of $riskTarget"))
    })
}

private def filterForRiskTarget(advisoryTag: AdvisoryTag, riskTarget: ModelPortfolioRiskTarget, p: ProductPortfolio): Boolean = {
  advisoryTag match {
    case AdvisoryTag.CORE_ENHANCED =>
      ProductPortfolio.extractCoreEnhancedMetaData(p).exists(_.riskTarget == riskTarget)
    case _ => false
  }
}
```

‌

I want to keep the method signature as close to the lookup by targetStockRatio one so it’s easier to switch later for Flagship/Esg/Factors/FlagshipDpm

**Source-preserving request, proposal, or question:**

> Maybe we can keep this method generic, but only handle for CoreEnhanced for now…
> 
> ```
> def findProductPortfolio(
>   advisoryTag: AdvisoryTag,
>   riskTarget: ModelPortfolioRiskTarget,
>   tradingAccountType: TradingAccountType
> ): Future[ProductPortfolio] = {
>   findAllActiveForAdvisoryTag(advisoryTag)
>     .filter(p => filterForTradingAccountType(advisoryTag, tradingAccountType, p))
>     .filter(p => filterForRiskTarget(advisoryTag, riskTarget, p))
>     .runWith(Sink.headOption)
>     .flatMap({
>       case Some(productPortfolio) => Future.successful(productPortfolio)
>       case None =>
>         Future
>           .failed(BadRequest(s"Unable to find $advisoryTag portfolio for trading account $tradingAccountType with risk target of $riskTarget"))
>     })
> }
> 
> private def filterForRiskTarget(advisoryTag: AdvisoryTag, riskTarget: ModelPortfolioRiskTarget, p: ProductPortfolio): Boolean = {
>   advisoryTag match {
>     case AdvisoryTag.CORE_ENHANCED =>
>       ProductPortfolio.extractCoreEnhancedMetaData(p).exists(_.riskTarget == riskTarget)
>     case _ => false
>   }
> }
> ```
> 
> ‌
> 
> I want to keep the method signature as close to the lookup by targetStockRatio one so it’s easier to switch later for Flagship/Esg/Factors/FlagshipDpm

**Conditions and limits:**

- Initial proposed generic signature handles only CoreEnhanced and otherwise returns false; row 837 proposes completing other productlines via ProductPortfolio.riskTarget.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:821 · comment 523845974 · PR 9605 · 2024-07-22

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/db/repository/ProductPortfolioRepository.scala`

**Evidence:** anon-2.jsonl:821 · comment 523845974 · PR 9605 · 2024-07-22

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/db/repository/ProductPortfolioRepository.scala`

**Explicit source context (pr_title):**

> [INV-3236] feat(advisory): create advisory endpoints for goal create

## A2-0826 — AdvisedGoalCreateHelper: Let’s make these 3 remote calls to portfolio/composition/performance run in parallel

**Source stance:** suggestion

**Context:**

> PR 9605 ([INV-3236] feat(advisory): create advisory endpoints for goal create), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/AdvisedGoalCreateHelper.scala; original row 826.

**Concern stated in the source:** Let’s make these 3 remote calls to portfolio/composition/performance run in parallel

**Source-preserving request, proposal, or question:**

> Let’s make these 3 remote calls to portfolio/composition/performance run in parallel

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:826 · comment 523842285 · PR 9605 · 2024-07-22

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/AdvisedGoalCreateHelper.scala`

**Evidence:** anon-2.jsonl:826 · comment 523842285 · PR 9605 · 2024-07-22

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/AdvisedGoalCreateHelper.scala`

**Explicit source context (pr_title):**

> [INV-3236] feat(advisory): create advisory endpoints for goal create

## A2-0830 — AdvisedGoalCreateHelper: These 3 futures are still run sequentially if written like this

**Source stance:** suggestion

**Context:**

> PR 9605 ([INV-3236] feat(advisory): create advisory endpoints for goal create), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/AdvisedGoalCreateHelper.scala; original row 830.

**Concern stated in the source:** These 3 futures are still run sequentially if written like this

We will need to write it as

```
val portfolioFut = ...
val compostionFut = ...
val performanceFut = ...

for {
  portfolio <- portfolioFut
  composition <- compostionFut
  performance <- performanceFut
  ...
} yield ...
```

‌

**Source-preserving request, proposal, or question:**

> These 3 futures are still run sequentially if written like this
> 
> We will need to write it as
> 
> ```
> val portfolioFut = ...
> val compostionFut = ...
> val performanceFut = ...
> 
> for {
>   portfolio <- portfolioFut
>   composition <- compostionFut
>   performance <- performanceFut
>   ...
> } yield ...
> ```
> 
> ‌

**Conditions and limits:**

- Declaring the three futures before for-comprehension starts portfolio/composition/performance work in parallel; the current sequencing does not.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:830 · comment 524568048 · PR 9605 · 2024-07-24

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/AdvisedGoalCreateHelper.scala`

**Evidence:** anon-2.jsonl:830 · comment 524568048 · PR 9605 · 2024-07-24

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/AdvisedGoalCreateHelper.scala`

**Explicit source context (pr_title):**

> [INV-3236] feat(advisory): create advisory endpoints for goal create

## A2-0836 — CustomerStatusHelper: Can we make this change for HK too

**Source stance:** suggestion

**Context:**

> PR 9605 ([INV-3236] feat(advisory): create advisory endpoints for goal create), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/CustomerStatusHelper.scala; original row 836.

**Concern stated in the source:** Can we make this change for HK too

I think no need to name them separately like current code

```
trait CustomerStatusHelper {
  def checkCustomerAiPiStatus(customerId: UUID): Future[Boolean]
}

trait SgCustomerStatusHelper extends CustomerStatusHelper with RegionSpecific[SilverRegion.Sg.type] {
  ...
}

trait HkCustomerStatusHelper extends CustomerStatusHelper with RegionSpecific[SilverRegion.Hk.type] {
  ...
}
```

‌

**Source-preserving request, proposal, or question:**

> Can we make this change for HK too
> 
> I think no need to name them separately like current code
> 
> ```
> trait CustomerStatusHelper {
>   def checkCustomerAiPiStatus(customerId: UUID): Future[Boolean]
> }
> 
> trait SgCustomerStatusHelper extends CustomerStatusHelper with RegionSpecific[SilverRegion.Sg.type] {
>   ...
> }
> 
> trait HkCustomerStatusHelper extends CustomerStatusHelper with RegionSpecific[SilverRegion.Hk.type] {
>   ...
> }
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:836 · comment 524566116 · PR 9605 · 2024-07-24

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/CustomerStatusHelper.scala`

**Evidence:** anon-2.jsonl:836 · comment 524566116 · PR 9605 · 2024-07-24

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/CustomerStatusHelper.scala`

**Explicit source context (pr_title):**

> [INV-3236] feat(advisory): create advisory endpoints for goal create

## A2-0839 — SgGoalCreatePortfolioSummaryBehaviour: Maybe consider grouping these futures so that we can run them in parallel as much as we can. There are many futures here, can make it very...

**Source stance:** suggestion

**Context:**

> PR 9605 ([INV-3236] feat(advisory): create advisory endpoints for goal create), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/sg/SgGoalCreatePortfolioSummaryBehaviour.scala; original row 839.

**Concern stated in the source:** Maybe consider grouping these futures so that we can run them in parallel as much as we can. There are many futures here, can make it very slow if running sequentially one by one

**Source-preserving request, proposal, or question:**

> Maybe consider grouping these futures so that we can run them in parallel as much as we can. There are many futures here, can make it very slow if running sequentially one by one

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:839 · comment 524908794 · PR 9605 · 2024-07-25

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/sg/SgGoalCreatePortfolioSummaryBehaviour.scala`

**Evidence:** anon-2.jsonl:839 · comment 524908794 · PR 9605 · 2024-07-25

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/sg/SgGoalCreatePortfolioSummaryBehaviour.scala`

**Explicit source context (pr_title):**

> [INV-3236] feat(advisory): create advisory endpoints for goal create

## A2-0879 — PortfolioFundLogic: Maybe `lazy val`?

**Source stance:** suggestion

**Context:**

> PR 9612 ([NE-282] (performance) make finding maa performance result true optional), performance-impl/src/main/scala/com/endowus/silver/performance/impl/logic/portfolio/impl/PortfolioFundLogic.scala; original row 879.

**Source-preserving request, proposal, or question:**

> Maybe `lazy val`?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:879 · comment 523828497 · PR 9612 · 2024-07-22

Source path: `performance-impl/src/main/scala/com/endowus/silver/performance/impl/logic/portfolio/impl/PortfolioFundLogic.scala`

**Evidence:** anon-2.jsonl:879 · comment 523828497 · PR 9612 · 2024-07-22

Source path: `performance-impl/src/main/scala/com/endowus/silver/performance/impl/logic/portfolio/impl/PortfolioFundLogic.scala`

**Explicit source context (pr_title):**

> [NE-282] (performance) make finding maa performance result true optional

## A2-0880 — ServiceLogicImpl: Should we add to FutureUtils… sth like `withTimer(timer: Timer, => T: Future[T])` and take care of proper start stop there? I suppose we don’t need to capture ...

**Source stance:** open-question

**Context:**

> PR 9525 ([INV-3185] feat(projection): Adhoc projection for queryPortfolioV4), projection-impl/src/main/scala/com/endowus/silver/projection/impl/logic/service/ServiceLogicImpl.scala; original row 880.

**Concern stated in the source:** Should we add to FutureUtils… sth like `withTimer(timer: Timer, => T: Future[T])` and take care of proper start stop there? I suppose we don’t need to capture for the `multiCcySimulationBatchManager.runAdHoc*Simulation` calls and not others?

**Source-preserving request, proposal, or question:**

> Should we add to FutureUtils… sth like `withTimer(timer: Timer, => T: Future[T])` and take care of proper start stop there? I suppose we don’t need to capture for the `multiCcySimulationBatchManager.runAdHoc*Simulation` calls and not others?

**Conditions and limits:**

- Timer helper needs by-name Future construction so it measures the intended work; the question also asks why only selected calls are timed.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:880 · comment 520053076 · PR 9525 · 2024-07-11

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/logic/service/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:880 · comment 520053076 · PR 9525 · 2024-07-11

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/logic/service/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-3185] feat(projection): Adhoc projection for queryPortfolioV4

## A2-0881 — ServiceLogicImpl: A bit late to call with withTimer here cuz the future already started when you define above

**Source stance:** explanation

**Context:**

> PR 9525 ([INV-3185] feat(projection): Adhoc projection for queryPortfolioV4), projection-impl/src/main/scala/com/endowus/silver/projection/impl/logic/service/ServiceLogicImpl.scala; original row 881.

**Concern stated in the source:** A bit late to call with withTimer here cuz the future already started when you define above

**Source-preserving request, proposal, or question:**

> A bit late to call with withTimer here cuz the future already started when you define above

**Conditions and limits:**

- The future has already started before the shown withTimer use.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:881 · comment 520924007 · PR 9525 · 2024-07-15

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/logic/service/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:881 · comment 520924007 · PR 9525 · 2024-07-15

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/logic/service/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-3185] feat(projection): Adhoc projection for queryPortfolioV4

## A2-0906 — allInvestmentGoalsPage: You can have both

**Source stance:** suggestion

**Context:**

> PR 9240 ([INV-3011] feat(report): Generate semi annual report), report-impl/src/main/resources/templates/hk/allInvestmentGoalsPage.html; original row 906.

**Source-preserving request, proposal, or question:**

> You can have both
> 
> ```
> case class PageData(
>   ...,
>   statementType: StatementTypeEnum
> ) {
>   lazy val isDpmSemiAnnualReport: Boolean = statementType == StatementTypeEnum.DPM_SEMI_ANNUAL_REPORT
> }
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:906 · comment 512145588 · PR 9240 · 2024-06-20

Source path: `report-impl/src/main/resources/templates/hk/allInvestmentGoalsPage.html`

**Evidence:** anon-2.jsonl:906 · comment 512145588 · PR 9240 · 2024-06-20

Source path: `report-impl/src/main/resources/templates/hk/allInvestmentGoalsPage.html`

**Explicit source context (pr_title):**

> [INV-3011] feat(report): Generate semi annual report

## A2-0982 — SgComplianceChecker: recoverWith should just return `Future.failed(exception)`. Can you help me change for cka one as well :pray:

**Source stance:** suggestion

**Context:**

> PR 9262 (TT-4461 Investment calling checkCustomerTradingRestrictionV3), investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/SgComplianceChecker.scala; original row 982.

**Concern stated in the source:** recoverWith should just return `Future.failed(exception)`. Can you help me change for cka one as well :pray:

**Source-preserving request, proposal, or question:**

> recoverWith should just return `Future.failed(exception)`. Can you help me change for cka one as well :pray:

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:982 · comment 507982158 · PR 9262 · 2024-06-04

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/SgComplianceChecker.scala`

**Evidence:** anon-2.jsonl:982 · comment 507982158 · PR 9262 · 2024-06-04

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/SgComplianceChecker.scala`

**Explicit source context (pr_title):**

> TT-4461 Investment calling checkCustomerTradingRestrictionV3

## A2-0991 — SgComplianceChecker: Let’s use `Future.failed` for `recoverWith`

**Source stance:** suggestion

**Context:**

> PR 9264 (TT-4463 Rebalance calling checkCustomerTradingRestrictionV3), rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/utils/sg/SgComplianceChecker.scala; original row 991.

**Concern stated in the source:** Let’s use `Future.failed` for `recoverWith`

**Source-preserving request, proposal, or question:**

> Let’s use `Future.failed` for `recoverWith`

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:991 · comment 507983004 · PR 9264 · 2024-06-04

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/utils/sg/SgComplianceChecker.scala`

**Evidence:** anon-2.jsonl:991 · comment 507983004 · PR 9264 · 2024-06-04

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/utils/sg/SgComplianceChecker.scala`

**Explicit source context (pr_title):**

> TT-4463 Rebalance calling checkCustomerTradingRestrictionV3

## A2-1002 — NotifyRebalanceTradeSettlementAmendedCmdHandler: If buy trade has not started, and we amend totalSoldAmount but keeping cashReservation intact, we might run into additional cash...

**Source stance:** suggestion

**Context:**

> PR 9365 (Feat/INV-3015 rebalance trade settlement amended), rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/NotifyRebalanceTradeSettlementAmendedCmdHandler.scala; original row 1002.

**Concern stated in the source:** If buy trade has not started, and we amend totalSoldAmount but keeping cashReservation intact, we might run into additional cash reservation for diff amount if we amend up.

So let’s log error and skip this `SELL_TRADE_SETTLED_AWAITING_BUY_PROCESS_TO_BEGIN`

**Source-preserving request, proposal, or question:**

> If buy trade has not started, and we amend totalSoldAmount but keeping cashReservation intact, we might run into additional cash reservation for diff amount if we amend up.
> 
> So let’s log error and skip this `SELL_TRADE_SETTLED_AWAITING_BUY_PROCESS_TO_BEGIN`

**Conditions and limits:**

- Exception to broad status allowance: SELL_TRADE_SETTLED_AWAITING_BUY_PROCESS_TO_BEGIN may create extra diff reservation on an upward amendment; log error and skip.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1002 · comment 514086416 · PR 9365 · 2024-06-27

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/NotifyRebalanceTradeSettlementAmendedCmdHandler.scala`

**Evidence:** anon-2.jsonl:1002 · comment 514086416 · PR 9365 · 2024-06-27

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/NotifyRebalanceTradeSettlementAmendedCmdHandler.scala`

**Explicit source context (pr_title):**

> Feat/INV-3015 rebalance trade settlement amended

## A2-1034 — AdvisedPortfolioOfferingsManager: Because `getPriceCcy` might throw, and we want all exceptions are thrown in Future so that it’s more predictable for caller. And since `getPric...

**Source stance:** explanation

**Context:**

> PR 9406 ([INV-3215] feat(advisory): Use performance metrics directly from performance svc for portfolio-offerings), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/AdvisedPortfolioOfferingsManager.scala; original row 1034.

**Concern stated in the source:** Because `getPriceCcy` might throw, and we want all exceptions are thrown in Future so that it’s more predictable for caller. And since `getPriceCcy` is in future, by rule of aesthetic symmetry, all 3 should be in :rofl:

**Source-preserving request, proposal, or question:**

> Because `getPriceCcy` might throw, and we want all exceptions are thrown in Future so that it’s more predictable for caller. And since `getPriceCcy` is in future, by rule of aesthetic symmetry, all 3 should be in :rofl:

**Conditions and limits:**

- getPriceCcy may throw synchronously, so it is moved into Future to make exception delivery predictable; symmetric treatment of all three calls is a stylistic reason.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1034 · comment 512945642 · PR 9406 · 2024-06-24

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/AdvisedPortfolioOfferingsManager.scala`

**Evidence:** anon-2.jsonl:1034 · comment 512945642 · PR 9406 · 2024-06-24

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/AdvisedPortfolioOfferingsManager.scala`

**Explicit source context (pr_title):**

> [INV-3215] feat(advisory): Use performance metrics directly from performance svc for portfolio-offerings

## A2-1045 — PlanCommunicationV2EventProcessor: In anticipation for more custom interpolations in future, we can change this a little to below \(similar to locale specific one\)

**Source stance:** suggestion

**Context:**

> PR 9206 (TT-4229 - recurring autofund investment schedule created comms), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala; original row 1045.

**Concern stated in the source:** In anticipation for more custom interpolations in future, we can change this a little to below \(similar to locale specific one\)

```
val commonInterpolations = Seq(...)
val autoFundInterpolations = recurringFundingInstructionDetails.autoFundDetails match {
  case Some(autoFundDetails) => Seq(...)
  case None => Seq.empty
}
<more custom interpolations go here>
commonInterpolations ++ autoFundInterpolations
```

‌

**Source-preserving request, proposal, or question:**

> In anticipation for more custom interpolations in future, we can change this a little to below \(similar to locale specific one\)
> 
> ```
> val commonInterpolations = Seq(...)
> val autoFundInterpolations = recurringFundingInstructionDetails.autoFundDetails match {
>   case Some(autoFundDetails) => Seq(...)
>   case None => Seq.empty
> }
> <more custom interpolations go here>
> commonInterpolations ++ autoFundInterpolations
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1045 · comment 510029419 · PR 9206 · 2024-06-12

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Evidence:** anon-2.jsonl:1045 · comment 510029419 · PR 9206 · 2024-06-12

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Explicit source context (pr_title):**

> TT-4229 - recurring autofund investment schedule created comms

## A2-1047 — HkGoalCreateRequest: Can be lazy val? Same for plan upsert request

**Source stance:** suggestion

**Context:**

> PR 9326 ([INV-3129] fix(advisory): auto acknowledge recurring ack for flagship dpm add goal and plan upsert flows), advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/hk/HkGoalCreateRequest.scala; original row 1047.

**Concern stated in the source:** Can be lazy val? Same for plan upsert request

**Source-preserving request, proposal, or question:**

> Can be lazy val? Same for plan upsert request

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1047 · comment 508970878 · PR 9326 · 2024-06-07

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/hk/HkGoalCreateRequest.scala`

**Evidence:** anon-2.jsonl:1047 · comment 508970878 · PR 9326 · 2024-06-07

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/hk/HkGoalCreateRequest.scala`

**Explicit source context (pr_title):**

> [INV-3129] fix(advisory): auto acknowledge recurring ack for flagship dpm add goal and plan upsert flows

## A2-1068 — PlanTraderEventProcessor: Can we log more on how to recover from here? e.g investigate \+ manually retry OR simply cancel trade

**Source stance:** suggestion

**Context:**

> PR 9299 (TT-4508 Validate supported currencies when making indicative quote), trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/PlanTraderEventProcessor.scala; original row 1068.

**Concern stated in the source:** Can we log more on how to recover from here? e.g investigate \+ manually retry OR simply cancel trade

**Source-preserving request, proposal, or question:**

> Can we log more on how to recover from here? e.g investigate \+ manually retry OR simply cancel trade

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1068 · comment 509688474 · PR 9299 · 2024-06-11

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/PlanTraderEventProcessor.scala`

**Evidence:** anon-2.jsonl:1068 · comment 509688474 · PR 9299 · 2024-06-11

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/PlanTraderEventProcessor.scala`

**Explicit source context (pr_title):**

> TT-4508 Validate supported currencies when making indicative quote

## A2-1088 — HkGoalModifySummaryBehaviour: All of these calls can run in parallel. You can try using `FutureUtils.zip`. Should be able to find similar code for SG flow

**Source stance:** suggestion

**Context:**

> PR 9213 (Feat/INV-2797/flagship dpm modify goal), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalmodify/hk/HkGoalModifySummaryBehaviour.scala; original row 1088.

**Concern stated in the source:** All of these calls can run in parallel. You can try using `FutureUtils.zip`. Should be able to find similar code for SG flow

**Source-preserving request, proposal, or question:**

> All of these calls can run in parallel. You can try using `FutureUtils.zip`. Should be able to find similar code for SG flow

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1088 · comment 505707043 · PR 9213 · 2024-05-29

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalmodify/hk/HkGoalModifySummaryBehaviour.scala`

**Evidence:** anon-2.jsonl:1088 · comment 505707043 · PR 9213 · 2024-05-29

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalmodify/hk/HkGoalModifySummaryBehaviour.scala`

**Explicit source context (pr_title):**

> Feat/INV-2797/flagship dpm modify goal

## A2-1099 — InstrumentUpsertManagerV2: No need to create new future right?

**Source stance:** suggestion

**Context:**

> PR 9014 (Resolve INV-2980: BE changes needed for admin instrument screens), instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentUpsertManagerV2.scala; original row 1099.

**Concern stated in the source:** No need to create new future right?

```
.transform(_ => Done, ex => BadRequest(ex.getMessage))
```

‌

**Source-preserving request, proposal, or question:**

> No need to create new future right?
> 
> ```
> .transform(_ => Done, ex => BadRequest(ex.getMessage))
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1099 · comment 499488283 · PR 9014 · 2024-05-09

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentUpsertManagerV2.scala`

**Evidence:** anon-2.jsonl:1099 · comment 499488283 · PR 9014 · 2024-05-09

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentUpsertManagerV2.scala`

**Explicit source context (pr_title):**

> Resolve INV-2980: BE changes needed for admin instrument screens

## A2-1147 — HkGoalCreateRequest: Should all these be `lazy val`?

**Source stance:** open-question

**Context:**

> PR 9015 (Resolve INV-2389: Add new add goal request for UTT.), advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/hk/HkGoalCreateRequest.scala; original row 1147.

**Source-preserving request, proposal, or question:**

> Should all these be `lazy val`?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1147 · comment 499489551 · PR 9015 · 2024-05-09

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/hk/HkGoalCreateRequest.scala`

**Evidence:** anon-2.jsonl:1147 · comment 499489551 · PR 9015 · 2024-05-09

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/hk/HkGoalCreateRequest.scala`

**Explicit source context (pr_title):**

> Resolve INV-2389: Add new add goal request for UTT.

## A2-1161 — SgFundSmartManagerV3: Maybe just extract this to the common `FundSmartInstrumentBuilder` ?

**Source stance:** suggestion

**Context:**

> PR 9218 (Feat/INV-3063 filter instrument fund document non ai), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgFundSmartManagerV3.scala; original row 1161.

**Concern stated in the source:** Maybe just extract this to the common `FundSmartInstrumentBuilder` ?

```
protected def filterAiPiSensitiveData(instrument: InstrumentInfoDto, isCustomerEligibleToViewAiPiDataFut: => Future[Boolean]): Future[InstrumentInfoDto] = {
  ...
}
```

‌

**Source-preserving request, proposal, or question:**

> Maybe just extract this to the common `FundSmartInstrumentBuilder` ?
> 
> ```
> protected def filterAiPiSensitiveData(instrument: InstrumentInfoDto, isCustomerEligibleToViewAiPiDataFut: => Future[Boolean]): Future[InstrumentInfoDto] = {
>   ...
> }
> ```
> 
> ‌

**Conditions and limits:**

- Use by-name isCustomerEligibleToViewAiPiDataFut in common FundSmartInstrumentBuilder helper.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1161 · comment 504108915 · PR 9218 · 2024-05-27

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgFundSmartManagerV3.scala`

**Evidence:** anon-2.jsonl:1161 · comment 504108915 · PR 9218 · 2024-05-27

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgFundSmartManagerV3.scala`

**Explicit source context (pr_title):**

> Feat/INV-3063 filter instrument fund document non ai

## A2-1197 — InstrumentExportScheduler: You can just batch it here

**Source stance:** suggestion

**Context:**

> PR 9073 (TT-4242 Automate export of Broker transactions for alts), broker-impl/src/main/scala/com/endowus/silver/broker/impl/utils/exportscheduler/InstrumentExportScheduler.scala; original row 1197.

**Concern stated in the source:** You can just batch it here

```
Source(instruments)
  .grouped(10)
  .map(_.toSet)
  .mapAsync(2) { instrumentIds =>
    instrumentSvc.getInstrumentV2ByIds(instrumentIds.mkString(",")).invoke().map(_.toList)
  }
  .flatMapConcat(Source(_))
  .runWith(Sink.seq)
```

‌

**Source-preserving request, proposal, or question:**

> You can just batch it here
> 
> ```
> Source(instruments)
>   .grouped(10)
>   .map(_.toSet)
>   .mapAsync(2) { instrumentIds =>
>     instrumentSvc.getInstrumentV2ByIds(instrumentIds.mkString(",")).invoke().map(_.toList)
>   }
>   .flatMapConcat(Source(_))
>   .runWith(Sink.seq)
> ```
> 
> ‌

**Conditions and limits:**

- Exact batching proposal: grouped(10), toSet, mapAsync(2), getInstrumentV2ByIds comma list, flatMapConcat, Sink.seq.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1197 · comment 500780169 · PR 9073 · 2024-05-14

Source path: `broker-impl/src/main/scala/com/endowus/silver/broker/impl/utils/exportscheduler/InstrumentExportScheduler.scala`

**Evidence:** anon-2.jsonl:1197 · comment 500780169 · PR 9073 · 2024-05-14

Source path: `broker-impl/src/main/scala/com/endowus/silver/broker/impl/utils/exportscheduler/InstrumentExportScheduler.scala`

**Explicit source context (pr_title):**

> TT-4242 Automate export of Broker transactions for alts

## A2-1204 — HttpServerStartup: Should we make `route` and `rejectionHandler` available in the base Endpoints? Then we provide overloading constructors, so service doesn’t need to think too ...

**Source stance:** suggestion

**Context:**

> PR 9049 (DYNAMIC-1046: Terminate service if onMemberUp fails (ready for review)), akka-http-commons/src/main/scala/com/endowus/silver/server/akka/http/HttpServerStartup.scala; original row 1204.

**Concern stated in the source:** Should we make `route` and `rejectionHandler` available in the base Endpoints? Then we provide overloading constructors, so service doesn’t need to think too much if their use case is standard, but still have an easy way to give additional routes if needed \(e.g. OpenApi route\)

```
class HttpServerStartup private(actorSystem: ActorSystem[_], endpoints: BaseEndpointResultCompat, routes: Route) {
  implicit val executionContext: ExecutionContext = actorSystem.executionContext
  implicit val rejectionHandler: RejectionHandler = endpoints.rejectionHandler
  
  def start(): Future[Unit] = {
    ...
  }
}

object HttpServerStartup {
  def apply(actorSystem: ActorSystem[_], endpoints: BaseEndpointResultCompat, additionalRoutes: Route*): HttpServerStartup = {
    val routes = ... // concat endpoints.routes and additionalRoutes
    new HttpServerStartup(actorSystem, endpoints, routes)
  }
}
```

‌

**Source-preserving request, proposal, or question:**

> Should we make `route` and `rejectionHandler` available in the base Endpoints? Then we provide overloading constructors, so service doesn’t need to think too much if their use case is standard, but still have an easy way to give additional routes if needed \(e.g. OpenApi route\)
> 
> ```
> class HttpServerStartup private(actorSystem: ActorSystem[_], endpoints: BaseEndpointResultCompat, routes: Route) {
>   implicit val executionContext: ExecutionContext = actorSystem.executionContext
>   implicit val rejectionHandler: RejectionHandler = endpoints.rejectionHandler
>   
>   def start(): Future[Unit] = {
>     ...
>   }
> }
> 
> object HttpServerStartup {
>   def apply(actorSystem: ActorSystem[_], endpoints: BaseEndpointResultCompat, additionalRoutes: Route*): HttpServerStartup = {
>     val routes = ... // concat endpoints.routes and additionalRoutes
>     new HttpServerStartup(actorSystem, endpoints, routes)
>   }
> }
> ```
> 
> ‌

**Conditions and limits:**

- Base endpoints can expose routes/rejectionHandler and constructors add extra routes such as OpenApi; this is proposed API design.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1204 · comment 499728704 · PR 9049 · 2024-05-10

Source path: `akka-http-commons/src/main/scala/com/endowus/silver/server/akka/http/HttpServerStartup.scala`

**Evidence:** anon-2.jsonl:1204 · comment 499728704 · PR 9049 · 2024-05-10

Source path: `akka-http-commons/src/main/scala/com/endowus/silver/server/akka/http/HttpServerStartup.scala`

**Explicit source context (pr_title):**

> DYNAMIC-1046: Terminate service if onMemberUp fails (ready for review)

## A2-1229 — HkComplianceHelperImpl: mapAsync\(2\)

**Source stance:** suggestion

**Context:**

> PR 9082 (Feat/INV-2598 duplicate goal name handling), goal-impl/src/main/scala/com/endowus/silver/goal/impl/helpers/hk/HkComplianceHelperImpl.scala; original row 1229.

**Source-preserving request, proposal, or question:**

> mapAsync\(2\)

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- Source requests mapAsync(2) specifically in HkComplianceHelperImpl; do not apply it to ordered same-partition Kafka subscribers.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1229 · comment 498860347 · PR 9082 · 2024-05-07

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/helpers/hk/HkComplianceHelperImpl.scala`

**Evidence:** anon-2.jsonl:1229 · comment 498860347 · PR 9082 · 2024-05-07

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/helpers/hk/HkComplianceHelperImpl.scala`

**Explicit source context (hunk):**

>  import scala.collection.immutable
>  import scala.concurrent.{ExecutionContext, Future}
>  
> -class HkComplianceValidatorImpl(val complianceService: HkComplianceService)(
> +class HkComplianceHelperImpl(val complianceService: HkComplianceService)(
>    implicit val ec: ExecutionContext,
>    val mat: Materializer,

**Evidence:** anon-2.jsonl:1229 · comment 498860347 · PR 9082 · 2024-05-07

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/helpers/hk/HkComplianceHelperImpl.scala`

**Explicit source context (pr_title):**

> Feat/INV-2598 duplicate goal name handling

## A2-1239 — DetectExpiredInvestmentRequestProcessor: [person] [person] [person] Is the below correct understanding?

**Source stance:** open-question

**Context:**

> PR 8955 (TT-4210 investment request expiry detection skip for auto funding), investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/DetectExpiredInvestmentRequestProcessor.scala; original row 1239.

**Concern stated in the source:** [person] [person] [person] Is the below correct understanding?

* autofx: If `fxConversionRequestId` is available here, it means cash is reserved for fx conversion, and we will ensure the conversion will happen. Hence, we will not expire the investment, regardless of `isRequestExpired`. If for whatever reason, the conversion cannot happen,  investment is cancelled elsewhere \(with adequate alerts if needs to manually cancel\).
* autofund: if `autoFundInstruction` is available here, we will ensure the deposit will happen. If there are failures, retry logic will consider expiry \+ cutOff into retry date. Hence, we will not expire the investment, regardless of `isRequestExpired`. And similarly, if for whatever reason, the deposit cannot happen,  investment is cancelled elsewhere \(with adequate alerts if needs to manually cancel\).

‌

If correct, can you please help to add this explanation here, so that it’s easy to understand this logic in future :pray: 

‌

**Source-preserving request, proposal, or question:**

> [person] [person] [person] Is the below correct understanding?
> 
> * autofx: If `fxConversionRequestId` is available here, it means cash is reserved for fx conversion, and we will ensure the conversion will happen. Hence, we will not expire the investment, regardless of `isRequestExpired`. If for whatever reason, the conversion cannot happen,  investment is cancelled elsewhere \(with adequate alerts if needs to manually cancel\).
> * autofund: if `autoFundInstruction` is available here, we will ensure the deposit will happen. If there are failures, retry logic will consider expiry \+ cutOff into retry date. Hence, we will not expire the investment, regardless of `isRequestExpired`. And similarly, if for whatever reason, the deposit cannot happen,  investment is cancelled elsewhere \(with adequate alerts if needs to manually cancel\).
> 
> ‌
> 
> If correct, can you please help to add this explanation here, so that it’s easy to understand this logic in future :pray: 
> 
> ‌

**Conditions and limits:**

- The complete autofx/autofund expiry model is explicitly presented for confirmation. Do not convert it to a settled guarantee: cancellation elsewhere, retry cutoff/expiry handling and manual alerts remain assumptions under review.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1239 · comment 498409421 · PR 8955 · 2024-05-06

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/DetectExpiredInvestmentRequestProcessor.scala`

> Is the below correct understanding?
> 
> * autofx: If `fxConversionRequestId` is available here, it means cash is reserved for fx conversion, and we will ensure the conversion will happen. Hence, we will not expire the investment, regardless of `isRequestExpired`. If for whatever reason, the conversion cannot happen,  investment is cancelled elsewhere \(with adequate alerts if needs to manually cancel\).
> * autofund: if `autoFundInstruction` is available here, we will ensure the deposit will happen. If there are failures, retry logic will consider expiry \+ cutOff into retry date. Hence, we will not expire the investment, regardless of `isRequestExpired`. And similarly, if for whatever reason, the deposit cannot happen,  investment is cancelled elsewhere \(with adequate alerts if needs to manually cancel\).
> 
> ‌
> 
> If correct, can you please help to add this explanation here, so that it’s easy to understand this logic in future :pray: 
> 
> ‌

**Evidence:** anon-2.jsonl:1239 · comment 498409421 · PR 8955 · 2024-05-06

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/DetectExpiredInvestmentRequestProcessor.scala`

**Explicit source context (pr_title):**

> TT-4210 investment request expiry detection skip for auto funding

## A2-1277 — HkGoalCreateRequest: Consider changing all these `def` to `lazy val` instead. No need to resolve them again.

**Source stance:** suggestion

**Context:**

> PR 8933 (Feat/INV-2808/flagship dpm goal create endpoints), advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/hk/HkGoalCreateRequest.scala; original row 1277.

**Source-preserving request, proposal, or question:**

> Consider changing all these `def` to `lazy val` instead. No need to resolve them again.

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1277 · comment 498011901 · PR 8933 · 2024-05-03

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/hk/HkGoalCreateRequest.scala`

**Evidence:** anon-2.jsonl:1277 · comment 498011901 · PR 8933 · 2024-05-03

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/hk/HkGoalCreateRequest.scala`

**Explicit source context (pr_title):**

> Feat/INV-2808/flagship dpm goal create endpoints

## A2-1292 — ValidationHelpers: We can extract amount validation into a method

**Source stance:** suggestion

**Context:**

> PR 8933 (Feat/INV-2808/flagship dpm goal create endpoints), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/ValidationHelpers.scala; original row 1292.

**Concern stated in the source:** We can extract amount validation into a method

```
  def validateAmountRestriction(maybeAmount: Option[BigDecimal], maybeRestriction: Option[SubscriptionAmountRegulation], context: String): Future[Done] = {
    maybeRestriction match {
      case Some(restriction) =>
        val expectedAmount = adjustAmount(maybeAmount, restriction)
        if (maybeAmount != expectedAmount) {
          Future.failed(BadRequest(s"$context breaches amount restrictions: request $maybeAmount, expected $expectedAmount"))
        } else {
          Future.successful(Done)
        }
      case None =>
        Future.successful(Done)
    }
  }
```

‌

And let caller decide how to extract amount \+ restriction, then handle Option themselves.

We can additionally create another method to extract amount for `PlanInvestmentBasedRequest` or `PlanUpsertInvestmentBasedRequest` if needed

**Source-preserving request, proposal, or question:**

> We can extract amount validation into a method
> 
> ```
>   def validateAmountRestriction(maybeAmount: Option[BigDecimal], maybeRestriction: Option[SubscriptionAmountRegulation], context: String): Future[Done] = {
>     maybeRestriction match {
>       case Some(restriction) =>
>         val expectedAmount = adjustAmount(maybeAmount, restriction)
>         if (maybeAmount != expectedAmount) {
>           Future.failed(BadRequest(s"$context breaches amount restrictions: request $maybeAmount, expected $expectedAmount"))
>         } else {
>           Future.successful(Done)
>         }
>       case None =>
>         Future.successful(Done)
>     }
>   }
> ```
> 
> ‌
> 
> And let caller decide how to extract amount \+ restriction, then handle Option themselves.
> 
> We can additionally create another method to extract amount for `PlanInvestmentBasedRequest` or `PlanUpsertInvestmentBasedRequest` if needed

**Conditions and limits:**

- Caller extracts amount/restriction/context; absent restriction succeeds, otherwise adjustAmount computes expected Option amount and mismatch returns failed BadRequest.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1292 · comment 498407253 · PR 8933 · 2024-05-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/ValidationHelpers.scala`

**Evidence:** anon-2.jsonl:1292 · comment 498407253 · PR 8933 · 2024-05-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/ValidationHelpers.scala`

**Explicit source context (pr_title):**

> Feat/INV-2808/flagship dpm goal create endpoints

## A2-1294 — HkGoalCreateRequest: lazy val for these too?

**Source stance:** suggestion

**Context:**

> PR 8933 (Feat/INV-2808/flagship dpm goal create endpoints), advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/hk/HkGoalCreateRequest.scala; original row 1294.

**Source-preserving request, proposal, or question:**

> lazy val for these too?

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1294 · comment 498399325 · PR 8933 · 2024-05-06

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/hk/HkGoalCreateRequest.scala`

**Evidence:** anon-2.jsonl:1294 · comment 498399325 · PR 8933 · 2024-05-06

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/hk/HkGoalCreateRequest.scala`

**Explicit source context (hunk):**

> +    with TagBasedAdvisedPortfolioRequest {
> +
> +  @deprecated("use initialFundingInstructions", "EN-3026")
> +  lazy val initialInvestmentAmount: BigDecimal = initialFundingInstructions.map(getAmountInPlanCcy).getOrElse(0) // deprecated field
> +  @deprecated("use recurringInvestmentRequest", "EN-3026")
> +  lazy val monthlyInvestmentAmount: Option[BigDecimal] = None // deprecated field in PlanInvestmentBasedRequest, replaced by `recurringInvestmentRequest`
> +  @deprecated("use recurringInvestmentRequest", "EN-3026")

**Evidence:** anon-2.jsonl:1294 · comment 498399325 · PR 8933 · 2024-05-06

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/hk/HkGoalCreateRequest.scala`

**Explicit source context (pr_title):**

> Feat/INV-2808/flagship dpm goal create endpoints

## A2-1295 — ValidationHelpers: Just `Future[Done]` is sufficient. For all the methods in this class

**Source stance:** suggestion

**Context:**

> PR 8933 (Feat/INV-2808/flagship dpm goal create endpoints), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/ValidationHelpers.scala; original row 1295.

**Source-preserving request, proposal, or question:**

> Just `Future[Done]` is sufficient. For all the methods in this class

**Conditions and limits:**

- Future[Done] rather than singleton Done.type is sufficient for this class methods.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1295 · comment 498544062 · PR 8933 · 2024-05-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/ValidationHelpers.scala`

**Evidence:** anon-2.jsonl:1295 · comment 498544062 · PR 8933 · 2024-05-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/ValidationHelpers.scala`

**Explicit source context (pr_title):**

> Feat/INV-2808/flagship dpm goal create endpoints

## A2-1305 — Review: Reported non-full redemption rejection: RequestedAmount 150000 exceeded plan redeemable MV 99986.82 and full redemption threshold 96987.2154. The log blocks a request no...

**Source stance:** reported-verification

**Context:**

> PR 9066 ([INV-3023] feat(redemption): Check requestedAmount against plan's redeemable MV to validate isFullRedemption flag for amount-based redemption), no inline path; original row 1305.

**Source-preserving request, proposal, or question:**

> Reported non-full redemption rejection: RequestedAmount 150000 exceeded plan redeemable MV 99986.82 and full redemption threshold 96987.2154. The log blocks a request not marked full redemption.

**Conditions and limits:**

- Reported rejection checks amount-based request not marked full redemption against plan redeemable threshold; literal amounts are technical test values, planId is incidental.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1305 · comment 497955740 · PR 9066 · 2024-05-03

> Redemption rejects with log

**Evidence:** anon-2.jsonl:1305 · comment 497955740 · PR 9066 · 2024-05-03

> Blocking redemption from plan, as request is not full redemption, but requestedAmount exceeds plan's redeemable threshold.

**Evidence:** anon-2.jsonl:1305 · comment 497955740 · PR 9066 · 2024-05-03

> RequestedAmount: 150000

**Evidence:** anon-2.jsonl:1305 · comment 497955740 · PR 9066 · 2024-05-03

> Plan redeemable MV: 99986.82

**Evidence:** anon-2.jsonl:1305 · comment 497955740 · PR 9066 · 2024-05-03

> Full redemption threshold: 96987.2154

**Evidence:** anon-2.jsonl:1305 · comment 497955740 · PR 9066 · 2024-05-03

**Explicit source context (pr_title):**

> [INV-3023] feat(redemption): Check requestedAmount against plan's redeemable MV to validate isFullRedemption flag for amount-based redemption

## A2-1306 — CustomerStateUpdatedLogic: Maybe make them follow same style right?

**Source stance:** suggestion

**Context:**

> PR 9039 (Feat/INV-3007 react to cra downgrade dpm), compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/CustomerStateUpdatedLogic.scala; original row 1306.

**Concern stated in the source:** Maybe make them follow same style right?

either

```
case CraValidationOutput.CraCat3 =>
  Future.successful(true)
case CraValidationOutput.CraCat2 if isGoalDiscretionary(goal) =>
  Future.successful(true)
case CraValidationOutput.CraCat2 if allocationHelper.isComplexPortfolio(targetAllocation) =>
  Future.successful(true)
case _ =>
  Future.successful(false)
```

or

```
case CraValidationOutput.CraCat3 =>
  Future.successful(true)
case CraValidationOutput.CraCat2 =>
  Future.successful(isGoalDiscretionary(goal) || allocationHelper.isComplexPortfolio(targetAllocation))
case _ =>
  Future.successful(false)
```

‌

**Source-preserving request, proposal, or question:**

> Maybe make them follow same style right?
> 
> either
> 
> ```
> case CraValidationOutput.CraCat3 =>
>   Future.successful(true)
> case CraValidationOutput.CraCat2 if isGoalDiscretionary(goal) =>
>   Future.successful(true)
> case CraValidationOutput.CraCat2 if allocationHelper.isComplexPortfolio(targetAllocation) =>
>   Future.successful(true)
> case _ =>
>   Future.successful(false)
> ```
> 
> or
> 
> ```
> case CraValidationOutput.CraCat3 =>
>   Future.successful(true)
> case CraValidationOutput.CraCat2 =>
>   Future.successful(isGoalDiscretionary(goal) || allocationHelper.isComplexPortfolio(targetAllocation))
> case _ =>
>   Future.successful(false)
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1306 · comment 498417714 · PR 9039 · 2024-05-06

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/CustomerStateUpdatedLogic.scala`

**Evidence:** anon-2.jsonl:1306 · comment 498417714 · PR 9039 · 2024-05-06

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/CustomerStateUpdatedLogic.scala`

**Explicit source context (pr_title):**

> Feat/INV-3007 react to cra downgrade dpm

## A2-1311 — DividendTopicSubscriberV3: Added comment for the AbortCmd… from transaction pov, it doesnt need to know about the possible cases of pref here. In future, we might support for ca...

**Source stance:** explanation

**Context:**

> PR 9037 ([INV-3016] feat(dividend)(timeseries)(transaction): Support aborting dividend stuck in WithdrawalRequested), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriberV3.scala; original row 1311.

**Concern stated in the source:** Added comment for the AbortCmd… from transaction pov, it doesnt need to know about the possible cases of pref here. In future, we might support for cases if required

**Source-preserving request, proposal, or question:**

> Added comment for the AbortCmd… from transaction pov, it doesnt need to know about the possible cases of pref here. In future, we might support for cases if required

**Conditions and limits:**

- AbortCmd is outside normal dividend workflow; transaction need not know all possible distribution preferences unless future cases require it.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1311 · comment 497612570 · PR 9037 · 2024-05-02

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriberV3.scala`

**Evidence:** anon-2.jsonl:1311 · comment 497612570 · PR 9037 · 2024-05-02

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriberV3.scala`

**Explicit source context (pr_title):**

> [INV-3016] feat(dividend)(timeseries)(transaction): Support aborting dividend stuck in WithdrawalRequested

## A2-1314 — BaseTradabilityChecker: How about just take goalId here?

**Source stance:** suggestion

**Context:**

> PR 9007 (Feat/INV-2818 tradability check), investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/BaseTradabilityChecker.scala; original row 1314.

**Concern stated in the source:** How about just take goalId here?

* `isDividendReinvestmentAllowed` and `isManualInvestmentAllowed` takes `planId` and call `fetchPlan`… same as `isSubsequentInvestmentAllowed`
* then `isInvestmentAllowed` starts another fut to lookup isDpmGoal - in parallel with existing `customerFut` and `instrumentsFut`.. this method will now be in charge of looking up whatever data it needs to perform the validation

‌

**Source-preserving request, proposal, or question:**

> How about just take goalId here?
> 
> * `isDividendReinvestmentAllowed` and `isManualInvestmentAllowed` takes `planId` and call `fetchPlan`… same as `isSubsequentInvestmentAllowed`
> * then `isInvestmentAllowed` starts another fut to lookup isDpmGoal - in parallel with existing `customerFut` and `instrumentsFut`.. this method will now be in charge of looking up whatever data it needs to perform the validation
> 
> ‌

**Conditions and limits:**

- Tradability method should own parallel lookup of isDpmGoal alongside customer/instruments, while plan-level entrypoints use fetchPlan.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1314 · comment 496506943 · PR 9007 · 2024-04-29

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/BaseTradabilityChecker.scala`

**Evidence:** anon-2.jsonl:1314 · comment 496506943 · PR 9007 · 2024-04-29

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/BaseTradabilityChecker.scala`

**Explicit source context (pr_title):**

> Feat/INV-2818 tradability check

## A2-1315 — BaseTradabilityChecker: Let’s put the same retry logic as fetchPlan

**Source stance:** suggestion

**Context:**

> PR 9007 (Feat/INV-2818 tradability check), investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/BaseTradabilityChecker.scala; original row 1315.

**Source-preserving request, proposal, or question:**

> Let’s put the same retry logic as fetchPlan

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1315 · comment 496506983 · PR 9007 · 2024-04-29

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/BaseTradabilityChecker.scala`

**Evidence:** anon-2.jsonl:1315 · comment 496506983 · PR 9007 · 2024-04-29

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/BaseTradabilityChecker.scala`

**Explicit source context (pr_title):**

> Feat/INV-2818 tradability check

## A2-1356 — MarketDataUploader: I suppose we can fetch both of these in parallel

**Source stance:** suggestion

**Context:**

> PR 8931 ([INV-2849] create a reconcile job to check instrument prices), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; original row 1356.

**Source-preserving request, proposal, or question:**

> I suppose we can fetch both of these in parallel

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1356 · comment 493341620 · PR 8931 · 2024-04-17

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Evidence:** anon-2.jsonl:1356 · comment 493341620 · PR 8931 · 2024-04-17

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> [INV-2849] create a reconcile job to check instrument prices

## A2-1364 — MarketDataUploader: I was talking about this point `It will be picked up in the future when it's available`… if missing in the middle, I don’t think current code will fill in th...

**Source stance:** suggestion

**Context:**

> PR 8931 ([INV-2849] create a reconcile job to check instrument prices), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; original row 1364.

**Concern stated in the source:** I was talking about this point `It will be picked up in the future when it's available`… if missing in the middle, I don’t think current code will fill in the holes - it only update the missing latest prices

**Source-preserving request, proposal, or question:**

> I was talking about this point `It will be picked up in the future when it's available`… if missing in the middle, I don’t think current code will fill in the holes - it only update the missing latest prices

**Conditions and limits:**

- Future availability does not imply historical holes will be filled by a latest-only sync.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1364 · comment 494504559 · PR 8931 · 2024-04-22

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Evidence:** anon-2.jsonl:1364 · comment 494504559 · PR 8931 · 2024-04-22

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> [INV-2849] create a reconcile job to check instrument prices

## A2-1366 — MarketDataUploader: Nit: no need to start a Source from beginning I think

**Source stance:** suggestion

**Context:**

> PR 8931 ([INV-2849] create a reconcile job to check instrument prices), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; original row 1366.

**Concern stated in the source:** Nit: no need to start a Source from beginning I think

```
for {
  instruments <- instrumentIds match {
    ...
  }
  _ <- Source(instruments)
    .filter(... check pricing source)
    .mapAsync(...)
    .run() // consider using SourceUtils.RunWithReportingExt (it has some basic logging for progress/completion)
} yield Done
```

‌

**Source-preserving request, proposal, or question:**

> Nit: no need to start a Source from beginning I think
> 
> ```
> for {
>   instruments <- instrumentIds match {
>     ...
>   }
>   _ <- Source(instruments)
>     .filter(... check pricing source)
>     .mapAsync(...)
>     .run() // consider using SourceUtils.RunWithReportingExt (it has some basic logging for progress/completion)
> } yield Done
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1366 · comment 494946679 · PR 8931 · 2024-04-23

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Evidence:** anon-2.jsonl:1366 · comment 494946679 · PR 8931 · 2024-04-23

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> [INV-2849] create a reconcile job to check instrument prices

## A2-1367 — MarketDataUploader: If we propagate the failure in these places, it will stop the whole flow processing. I suppose we just want to skip?

**Source stance:** suggestion

**Context:**

> PR 8931 ([INV-2849] create a reconcile job to check instrument prices), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; original row 1367.

**Concern stated in the source:** If we propagate the failure in these places, it will stop the whole flow processing. I suppose we just want to skip?

If we use `runWithReporting`, we can potentially write sth like this

```
Source(instrument)
  .mapAsync(parallelism) { instrument =>
    reconcilePrices(instrument) // extract this whole pricing fetching + compare into a method
      .map(_ => Right(Done))
      .recover {
        case ex =>
          logger.error("meaningful log message", ex)
          Left(instrument.id)
      }
  }
  .runWithReporting("meaningful context")
```

‌

**Source-preserving request, proposal, or question:**

> If we propagate the failure in these places, it will stop the whole flow processing. I suppose we just want to skip?
> 
> If we use `runWithReporting`, we can potentially write sth like this
> 
> ```
> Source(instrument)
>   .mapAsync(parallelism) { instrument =>
>     reconcilePrices(instrument) // extract this whole pricing fetching + compare into a method
>       .map(_ => Right(Done))
>       .recover {
>         case ex =>
>           logger.error("meaningful log message", ex)
>           Left(instrument.id)
>       }
>   }
>   .runWithReporting("meaningful context")
> ```
> 
> ‌

**Conditions and limits:**

- Per-instrument failures should produce Left(instrument.id) and continue under runWithReporting, rather than fail whole reconciliation.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1367 · comment 494949025 · PR 8931 · 2024-04-23

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Evidence:** anon-2.jsonl:1367 · comment 494949025 · PR 8931 · 2024-04-23

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> [INV-2849] create a reconcile job to check instrument prices

## A2-1368 — MarketDataUploader: This method doesn’t need to return Future right? I have everything resolved already

**Source stance:** suggestion

**Context:**

> PR 8931 ([INV-2849] create a reconcile job to check instrument prices), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; original row 1368.

**Source-preserving request, proposal, or question:**

> This method doesn’t need to return Future right? I have everything resolved already

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1368 · comment 494950068 · PR 8931 · 2024-04-23

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Evidence:** anon-2.jsonl:1368 · comment 494950068 · PR 8931 · 2024-04-23

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> [INV-2849] create a reconcile job to check instrument prices

## A2-1370 — MarketDataUploader: It will propagate and stop the flow, cuz we put `Future.failed(ex)`, effectively rethrow the exception

**Source stance:** explanation

**Context:**

> PR 8931 ([INV-2849] create a reconcile job to check instrument prices), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; original row 1370.

**Concern stated in the source:** It will propagate and stop the flow, cuz we put `Future.failed(ex)`, effectively rethrow the exception

**Source-preserving request, proposal, or question:**

> It will propagate and stop the flow, cuz we put `Future.failed(ex)`, effectively rethrow the exception

**Conditions and limits:**

- Future.failed(ex) propagates/rethrows, stopping the stream if not recovered per item.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1370 · comment 494954527 · PR 8931 · 2024-04-23

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Evidence:** anon-2.jsonl:1370 · comment 494954527 · PR 8931 · 2024-04-23

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> [INV-2849] create a reconcile job to check instrument prices

## A2-1371 — MarketDataUploader: We log error outside in the `reconcileInstrumentsPrice` already. We can just wrap the exception here to avoid double sentry alerts

**Source stance:** suggestion

**Context:**

> PR 8931 ([INV-2849] create a reconcile job to check instrument prices), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; original row 1371.

**Concern stated in the source:** We log error outside in the `reconcileInstrumentsPrice` already. We can just wrap the exception here to avoid double sentry alerts

```
Future.failed(new Exception("Error fetching ....", ex))
```

‌

**Source-preserving request, proposal, or question:**

> We log error outside in the `reconcileInstrumentsPrice` already. We can just wrap the exception here to avoid double sentry alerts
> 
> ```
> Future.failed(new Exception("Error fetching ....", ex))
> ```
> 
> ‌

**Conditions and limits:**

- Wrap with context but log only once at outer reconcileInstrumentsPrice to avoid duplicate Sentry alerts.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1371 · comment 495203447 · PR 8931 · 2024-04-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Evidence:** anon-2.jsonl:1371 · comment 495203447 · PR 8931 · 2024-04-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> [INV-2849] create a reconcile job to check instrument prices

## A2-1380 — MarketDataUploader: This version will now run to completion before it returns Done, making the http endpoint waits for potentially long time.

**Source stance:** suggestion

**Context:**

> PR 8931 ([INV-2849] create a reconcile job to check instrument prices), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; original row 1380.

**Concern stated in the source:** This version will now run to completion before it returns Done, making the http endpoint waits for potentially long time.

We will need to change `MarketDataServiceImpl` to return immediately after we trigger the logic call

```
  def reconcileInstrumentsPrice(request: requests.ReconcileInstrumentsPriceRequest): Future[Done] = {
    logic.reconcileInstrumentsPrice(request)
    Future.successful(Done)
  }
```

‌

**Source-preserving request, proposal, or question:**

> This version will now run to completion before it returns Done, making the http endpoint waits for potentially long time.
> 
> We will need to change `MarketDataServiceImpl` to return immediately after we trigger the logic call
> 
> ```
>   def reconcileInstrumentsPrice(request: requests.ReconcileInstrumentsPriceRequest): Future[Done] = {
>     logic.reconcileInstrumentsPrice(request)
>     Future.successful(Done)
>   }
> ```
> 
> ‌

**Conditions and limits:**

- Awaiting full reconciliation holds HTTP open; proposed ServiceImpl starts the logic and immediately returns successful Done. This source-specific fire-and-forget suggestion must not be generalized to all asynchronous work.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1380 · comment 495250032 · PR 8931 · 2024-04-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Evidence:** anon-2.jsonl:1380 · comment 495250032 · PR 8931 · 2024-04-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> [INV-2849] create a reconcile job to check instrument prices

## A2-1398 — PortfolioUnderlyingManager: If you have time, can you help us change this `await` usage to the usual for-comprehend block too? All these lookup steps can be called in parallel, ...

**Source stance:** suggestion

**Context:**

> PR 8930 ([EN-3226] Add display tags to maa cards), portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/managers/PortfolioUnderlyingManager.scala; original row 1398.

**Concern stated in the source:** If you have time, can you help us change this `await` usage to the usual for-comprehend block too? All these lookup steps can be called in parallel, so let’s do that as well :pray:

**Source-preserving request, proposal, or question:**

> If you have time, can you help us change this `await` usage to the usual for-comprehend block too? All these lookup steps can be called in parallel, so let’s do that as well :pray:

**Conditions and limits:**

- Parallelizable lookups should replace await with for-comprehension after starting Futures.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1398 · comment 493296281 · PR 8930 · 2024-04-17

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/managers/PortfolioUnderlyingManager.scala`

**Evidence:** anon-2.jsonl:1398 · comment 493296281 · PR 8930 · 2024-04-17

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/managers/PortfolioUnderlyingManager.scala`

**Explicit source context (pr_title):**

> [EN-3226] Add display tags to maa cards

## A2-1399 — PortfolioUnderlyingManager: I suppose we can fetch composition and performance in parallel to save some time too

**Source stance:** suggestion

**Context:**

> PR 8930 ([EN-3226] Add display tags to maa cards), portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/managers/PortfolioUnderlyingManager.scala; original row 1399.

**Concern stated in the source:** I suppose we can fetch composition and performance in parallel to save some time too

```
val compositionFut = ...
val performanceFut = ...

for {
  composition <- compositionFut
  performance <- performanceFut
  ...
}
```

‌

**Source-preserving request, proposal, or question:**

> I suppose we can fetch composition and performance in parallel to save some time too
> 
> ```
> val compositionFut = ...
> val performanceFut = ...
> 
> for {
>   composition <- compositionFut
>   performance <- performanceFut
>   ...
> }
> ```
> 
> ‌

**Conditions and limits:**

- Start compositionFut and performanceFut before awaiting either.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1399 · comment 493305495 · PR 8930 · 2024-04-17

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/managers/PortfolioUnderlyingManager.scala`

**Evidence:** anon-2.jsonl:1399 · comment 493305495 · PR 8930 · 2024-04-17

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/managers/PortfolioUnderlyingManager.scala`

**Explicit source context (pr_title):**

> [EN-3226] Add display tags to maa cards

## A2-1414 — SubscriberHelpers: Avoid Option.get in general. I guess here you can write it as

**Source stance:** suggestion

**Context:**

> PR 8863 (Feat/INV-2784 transaction dpm goal related tagging), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/SubscriberHelpers.scala; original row 1414.

**Concern stated in the source:** Avoid Option.get in general. I guess here you can write it as

```
maybeExistingTransaction
  .map {
    case ...
  }
  .map(Future.successful)
  .getOrElse {
    advisoryClassification match ...
  }
```

‌

**Source-preserving request, proposal, or question:**

> Avoid Option.get in general. I guess here you can write it as
> 
> ```
> maybeExistingTransaction
>   .map {
>     case ...
>   }
>   .map(Future.successful)
>   .getOrElse {
>     advisoryClassification match ...
>   }
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1414 · comment 489255981 · PR 8863 · 2024-04-05

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/SubscriberHelpers.scala`

**Evidence:** anon-2.jsonl:1414 · comment 489255981 · PR 8863 · 2024-04-05

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/SubscriberHelpers.scala`

**Explicit source context (pr_title):**

> Feat/INV-2784 transaction dpm goal related tagging

## A2-1416 — PortfolioSuitabilityAnalysisRequest: As discussed, let’s not mention DPM in request type, and add it as a flag paired with each portfolioId instead, so we can reuse this for fut...

**Source stance:** suggestion

**Context:**

> PR 8834 (Feat/INV-2861 dpm portfolio suitability), compliance-api/src/main/scala/com/endowus/silver/compliance/api/requests/hk/portfolioSuitabilityAnalysis/PortfolioSuitabilityAnalysisRequest.scala; original row 1416.

**Concern stated in the source:** As discussed, let’s not mention DPM in request type, and add it as a flag paired with each portfolioId instead, so we can reuse this for future product lines in HK

**Source-preserving request, proposal, or question:**

> As discussed, let’s not mention DPM in request type, and add it as a flag paired with each portfolioId instead, so we can reuse this for future product lines in HK

**Conditions and limits:**

- DPM flag should pair with each portfolioId in a reusable request, rather than embed DPM in request type.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1416 · comment 488849291 · PR 8834 · 2024-04-04

Source path: `compliance-api/src/main/scala/com/endowus/silver/compliance/api/requests/hk/portfolioSuitabilityAnalysis/PortfolioSuitabilityAnalysisRequest.scala`

**Evidence:** anon-2.jsonl:1416 · comment 488849291 · PR 8834 · 2024-04-04

Source path: `compliance-api/src/main/scala/com/endowus/silver/compliance/api/requests/hk/portfolioSuitabilityAnalysis/PortfolioSuitabilityAnalysisRequest.scala`

**Explicit source context (pr_title):**

> Feat/INV-2861 dpm portfolio suitability

## A2-1419 — PortfolioSuitabilityAnalysisLogic: Doesn’t look like we need Future here

**Source stance:** open-question

**Context:**

> PR 8834 (Feat/INV-2861 dpm portfolio suitability), compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/PortfolioSuitabilityAnalysisLogic.scala; original row 1419.

**Source-preserving request, proposal, or question:**

> Doesn’t look like we need Future here

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1419 · comment 488849789 · PR 8834 · 2024-04-04

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/PortfolioSuitabilityAnalysisLogic.scala`

**Evidence:** anon-2.jsonl:1419 · comment 488849789 · PR 8834 · 2024-04-04

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/PortfolioSuitabilityAnalysisLogic.scala`

**Explicit source context (pr_title):**

> Feat/INV-2861 dpm portfolio suitability

## A2-1453 — BaseServiceLogicImpl: Better to use Source instead of Future.sequence, but ok a goal only at most 3 plans as of now. Can extract whole of this to a method instead of just `appen...

**Source stance:** suggestion

**Context:**

> PR 8677 ([EN-3097] Remove cassandra readside dependency in goal svc), goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala; original row 1453.

**Concern stated in the source:** Better to use Source instead of Future.sequence, but ok a goal only at most 3 plans as of now. Can extract whole of this to a method instead of just `appendPlanToGoal`

**Source-preserving request, proposal, or question:**

> Better to use Source instead of Future.sequence, but ok a goal only at most 3 plans as of now. Can extract whole of this to a method instead of just `appendPlanToGoal`

**Conditions and limits:**

- Source preferred Source to Future.sequence but explicitly allows current code because goal has at most 3 plans at that time.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1453 · comment 481432011 · PR 8677 · 2024-03-13

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:1453 · comment 481432011 · PR 8677 · 2024-03-13

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [EN-3097] Remove cassandra readside dependency in goal svc

## A2-1491 — TradeTopicSubscriber: Hmm I’m surprised we have so many `parallelism` = 2 in investment svc without the safeMapAsync… [person] speed should be fine here, we should just change t...

**Source stance:** suggestion

**Context:**

> PR 8764 (Feat/INV-2777 invest systems subscriber tracing), investment-impl/src/main/scala/com/endowus/silver/investment/impl/subscribers/TradeTopicSubscriber.scala; original row 1491.

**Concern stated in the source:** Hmm I’m surprised we have so many `parallelism` = 2 in investment svc without the safeMapAsync… [person] speed should be fine here, we should just change to 1 for safety yeah?

**Source-preserving request, proposal, or question:**

> Hmm I’m surprised we have so many `parallelism` = 2 in investment svc without the safeMapAsync… [person] speed should be fine here, we should just change to 1 for safety yeah?

**Conditions and limits:**

- Investment subscribers with parallelism=2 lack safeMapAsync; source proposes parallelism=1 for safety.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1491 · comment 484186784 · PR 8764 · 2024-03-22

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/subscribers/TradeTopicSubscriber.scala`

> Hmm I’m surprised we have so many `parallelism` = 2 in investment svc without the safeMapAsync…

**Evidence:** anon-2.jsonl:1491 · comment 484186784 · PR 8764 · 2024-03-22

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/subscribers/TradeTopicSubscriber.scala`

> speed should be fine here, we should just change to 1 for safety yeah?

**Evidence:** anon-2.jsonl:1491 · comment 484186784 · PR 8764 · 2024-03-22

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/subscribers/TradeTopicSubscriber.scala`

**Explicit source context (pr_title):**

> Feat/INV-2777 invest systems subscriber tracing

## A2-1502 — UpdateTradeFxConversionRequestIdCmdHandler: Are you planning to use same cmd handler for future cases of `fundingInstructions`?

**Source stance:** open-question

**Context:**

> PR 8663 (TT-3887 Update trade and investment request with queued FX conversion request ID), trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/UpdateTradeFxConversionRequestIdCmdHandler.scala; original row 1502.

**Concern stated in the source:** Are you planning to use same cmd handler for future cases of `fundingInstructions`?

* if yes, then probably should make this cmd \+ event a bit more generic
* otherwise, let’s also match Some\(\_\) and throw? And maybe rename this cmd \+ event to be a bit specific about fx id of this auto fx funding instructions.

Same suggestion on investment svc side

‌

**Source-preserving request, proposal, or question:**

> Are you planning to use same cmd handler for future cases of `fundingInstructions`?
> 
> * if yes, then probably should make this cmd \+ event a bit more generic
> * otherwise, let’s also match Some\(\_\) and throw? And maybe rename this cmd \+ event to be a bit specific about fx id of this auto fx funding instructions.
> 
> Same suggestion on investment svc side
> 
> ‌

**Conditions and limits:**

- If command will cover future funding instructions, make it generic; otherwise reject existing Some and name specifically for autofx id. Same consideration applies in investment service.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1502 · comment 481440066 · PR 8663 · 2024-03-13

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/UpdateTradeFxConversionRequestIdCmdHandler.scala`

**Evidence:** anon-2.jsonl:1502 · comment 481440066 · PR 8663 · 2024-03-13

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/UpdateTradeFxConversionRequestIdCmdHandler.scala`

**Explicit source context (pr_title):**

> TT-3887 Update trade and investment request with queued FX conversion request ID

## A2-1504 — TradingAccountEventProcessor: Does this actually return or it will simply assign Future\[Done\] to `brokerAccountId`?

**Source stance:** open-question

**Context:**

> PR 8663 (TT-3887 Update trade and investment request with queued FX conversion request ID), trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/tradingAccount/processors/TradingAccountEventProcessor.scala; original row 1504.

**Source-preserving request, proposal, or question:**

> Does this actually return or it will simply assign Future\[Done\] to `brokerAccountId`?

**Conditions and limits:**

- Concern is whether Future[Done] is actually returned or accidentally assigned to brokerAccountId; not a confirmed runtime outcome.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1504 · comment 482992743 · PR 8663 · 2024-03-19

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/tradingAccount/processors/TradingAccountEventProcessor.scala`

**Evidence:** anon-2.jsonl:1504 · comment 482992743 · PR 8663 · 2024-03-19

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/tradingAccount/processors/TradingAccountEventProcessor.scala`

**Explicit source context (pr_title):**

> TT-3887 Update trade and investment request with queued FX conversion request ID

## A2-1505 — TradingAccountEventProcessor: This is actually very dangerous if we add/move the fields around and if the type matches UUID, we won’t get any compilation error…

**Source stance:** suggestion

**Context:**

> PR 8663 (TT-3887 Update trade and investment request with queued FX conversion request ID), trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/tradingAccount/processors/TradingAccountEventProcessor.scala; original row 1505.

**Concern stated in the source:** This is actually very dangerous if we add/move the fields around and if the type matches UUID, we won’t get any compilation error…

Would this better?

```
  val tradeRelatedFut = (reservation.tradeId, reservation.requestedPlanId) match {
    case (Some(tradeId), Some(planId)) =>
      reservation.fxConversionRequestId match {
        case Some(fxConversionRequestId) =>
          // fx funded trade
        case None =>
          // normal trade
      }
    case _ =>
      logger.info("Ignoring blah")
      Future.successful(Done)
  }
```

‌

**Source-preserving request, proposal, or question:**

> This is actually very dangerous if we add/move the fields around and if the type matches UUID, we won’t get any compilation error…
> 
> Would this better?
> 
> ```
>   val tradeRelatedFut = (reservation.tradeId, reservation.requestedPlanId) match {
>     case (Some(tradeId), Some(planId)) =>
>       reservation.fxConversionRequestId match {
>         case Some(fxConversionRequestId) =>
>           // fx funded trade
>         case None =>
>           // normal trade
>       }
>     case _ =>
>       logger.info("Ignoring blah")
>       Future.successful(Done)
>   }
> ```
> 
> ‌

**Conditions and limits:**

- Same-typed UUID fields make positional extractor refactors compile while mixing meanings; explicitly match reservation.tradeId/requestedPlanId then fxConversionRequestId.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1505 · comment 483011526 · PR 8663 · 2024-03-19

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/tradingAccount/processors/TradingAccountEventProcessor.scala`

**Evidence:** anon-2.jsonl:1505 · comment 483011526 · PR 8663 · 2024-03-19

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/tradingAccount/processors/TradingAccountEventProcessor.scala`

**Explicit source context (pr_title):**

> TT-3887 Update trade and investment request with queued FX conversion request ID

## A2-1509 — PlanTraderEventProcessor: Maybe we should add that support should check if the queued fx indeed not created before retrying..

**Source stance:** open-question

**Context:**

> PR 8661 (TT-3483 Handle BUY trades with funding instructions), trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/PlanTraderEventProcessor.scala; original row 1509.

**Source-preserving request, proposal, or question:**

> Maybe we should add that support should check if the queued fx indeed not created before retrying..

**Conditions and limits:**

- Before retrying queued FX creation, support should verify it was not already created.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1509 · comment 483729361 · PR 8661 · 2024-03-21

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/PlanTraderEventProcessor.scala`

**Evidence:** anon-2.jsonl:1509 · comment 483729361 · PR 8661 · 2024-03-21

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/processors/PlanTraderEventProcessor.scala`

**Explicit source context (pr_title):**

> TT-3483 Handle BUY trades with funding instructions

## A2-1518 — HkFundSmartManager: Maybe use `InstrumentInfoDto.whitelistedGoalTypes` and check based on goal types instead? Follow similar approach for sg portfolio summary, cuz we will need ...

**Source stance:** suggestion

**Context:**

> PR 8619 (Resolve INV-2765: Endpoint to derive advisory questionnaire for a given set of instruments.), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/HkFundSmartManager.scala; original row 1518.

**Concern stated in the source:** Maybe use `InstrumentInfoDto.whitelistedGoalTypes` and check based on goal types instead? Follow similar approach for sg portfolio summary, cuz we will need to support RF exclusive instruments in HK in future

**Source-preserving request, proposal, or question:**

> Maybe use `InstrumentInfoDto.whitelistedGoalTypes` and check based on goal types instead? Follow similar approach for sg portfolio summary, cuz we will need to support RF exclusive instruments in HK in future

**Conditions and limits:**

- whitelistedGoalTypes supports future HK RF-exclusive instruments, following SG portfolio-summary approach.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1518 · comment 480916977 · PR 8619 · 2024-03-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/HkFundSmartManager.scala`

**Evidence:** anon-2.jsonl:1518 · comment 480916977 · PR 8619 · 2024-03-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/HkFundSmartManager.scala`

**Explicit source context (pr_title):**

> Resolve INV-2765: Endpoint to derive advisory questionnaire for a given set of instruments.

## A2-1521 — HkFundSmartManager: Nits: These 2 methods don’t have to return Future. We can just throw and keep return type as `Unit`

**Source stance:** suggestion

**Context:**

> PR 8619 (Resolve INV-2765: Endpoint to derive advisory questionnaire for a given set of instruments.), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/HkFundSmartManager.scala; original row 1521.

**Source-preserving request, proposal, or question:**

> Nits: These 2 methods don’t have to return Future. We can just throw and keep return type as `Unit`

**Conditions and limits:**

- For resolved synchronous validation, throw with Unit instead of unnecessary Future is proposed.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1521 · comment 481680009 · PR 8619 · 2024-03-14

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/HkFundSmartManager.scala`

**Evidence:** anon-2.jsonl:1521 · comment 481680009 · PR 8619 · 2024-03-14

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/HkFundSmartManager.scala`

**Explicit source context (pr_title):**

> Resolve INV-2765: Endpoint to derive advisory questionnaire for a given set of instruments.

## A2-1533 — FundSmartHelper: fee <- `estimateAccessFee`

**Source stance:** suggestion

**Context:**

> PR 8488 (Resolve INV-2640: Changes to include estimation for multi-fund goal access fee for single fund goal creation.), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/fundsmart/FundSmartHelper.scala; original row 1533.

**Concern stated in the source:** fee <- `estimateAccessFee`

maybeMulti <- if\(special\) `estimateAccessFeeSpecial` else Future\(None\)

yield case class

‌

**Source-preserving request, proposal, or question:**

> fee <- `estimateAccessFee`
> 
> maybeMulti <- if\(special\) `estimateAccessFeeSpecial` else Future\(None\)
> 
> yield case class
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1533 · comment 483363691 · PR 8488 · 2024-03-20

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/fundsmart/FundSmartHelper.scala`

**Evidence:** anon-2.jsonl:1533 · comment 483363691 · PR 8488 · 2024-03-20

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/fundsmart/FundSmartHelper.scala`

**Explicit source context (pr_title):**

> Resolve INV-2640: Changes to include estimation for multi-fund goal access fee for single fund goal creation.

## A2-1554 — RebalanceRequestTable: We missed a `v` for version here, but it’s consistent in V4 too :sweat_smile: we will change this when we upversion  this table again in future

**Source stance:** explanation

**Context:**

> PR 8646 (PLATFORM-535: Rebalance readside turn off gcp), rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/db/jdbc/RebalanceRequestTable.scala; original row 1554.

**Source-preserving request, proposal, or question:**

> We missed a `v` for version here, but it’s consistent in V4 too :sweat_smile: we will change this when we upversion  this table again in future

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- Missing v in existing index names is deliberately deferred until next upversion to preserve V4 consistency.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1554 · comment 481364880 · PR 8646 · 2024-03-13

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/db/jdbc/RebalanceRequestTable.scala`

**Evidence:** anon-2.jsonl:1554 · comment 481364880 · PR 8646 · 2024-03-13

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/db/jdbc/RebalanceRequestTable.scala`

**Explicit source context (hunk):**

> -  def indexGoalId = index(name = s"idx_rebalance_request_${version}_goal_id", on = goalId, unique = false)
> -  def indexPlanId = index(name = s"idx_rebalance_request_${version}_plan_id", on = planId, unique = false)
> -  def indexStatusReason = index(name = s"idx_rebalance_request_${version}_status_reason", on = (status, reason), unique = false)
> +  def indexCustomerId = index(name = RebalanceRequestTableV4.customerIdIndex, on = customerId, unique = false)
> +  def indexGoalId = index(name = RebalanceRequestTableV4.goalIdIndex, on = goalId, unique = false)
> +  def indexPlanId = index(name = RebalanceRequestTableV4.planIdIndex, on = planId, unique = false)
> +  def indexStatusReason = index(name = RebalanceRequestTableV4.statusReasonIndex, on = (status, reason), unique = false)

**Evidence:** anon-2.jsonl:1554 · comment 481364880 · PR 8646 · 2024-03-13

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/db/jdbc/RebalanceRequestTable.scala`

**Explicit source context (pr_title):**

> PLATFORM-535: Rebalance readside turn off gcp

## A2-1557 — SgFundSmartManagerV3: Yea that was good catch. This NotFound is thrown by our own `createFuture` :see_no_evil:

**Source stance:** explanation

**Context:**

> PR 8346 (Resolve INV-2436: Changes to include portfolio performance for illiquid alts.), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgFundSmartManagerV3.scala; original row 1557.

**Source-preserving request, proposal, or question:**

> Yea that was good catch. This NotFound is thrown by our own `createFuture` :see_no_evil:

**Conditions and limits:**

- Follow-up identifies the NotFound as locally thrown by createFuture, resolving row 1556 concern.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1557 · comment 480873856 · PR 8346 · 2024-03-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgFundSmartManagerV3.scala`

**Evidence:** anon-2.jsonl:1557 · comment 480873856 · PR 8346 · 2024-03-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgFundSmartManagerV3.scala`

**Explicit source context (pr_title):**

> Resolve INV-2436: Changes to include portfolio performance for illiquid alts.

## A2-1558 — FxWalletQuotationServiceImplSpec: It’s more about scaffeine behaviour, but I think it’s useful to capture this in a test

**Source stance:** suggestion

**Context:**

> PR 8496 (TT-3906 New API to get cached indicative FX rates), fxwallet-impl/src/test/scala/com/endowus/silver/fxwallet/impl/logic/service/FxWalletQuotationServiceImplSpec.scala; original row 1558.

**Concern stated in the source:** It’s more about scaffeine behaviour, but I think it’s useful to capture this in a test

‌

```
when(fxBrokerMock.createQuotation)
  .thenReturn(_ => Future.failed(new Exception("some error")))
  .thenReturn(_ => Future.successful(fxQuotation))
```

then make 2 calls to `getIndicativeFxQuotation` and verify the error is not cached, and that 2nd call will get successful response

**Source-preserving request, proposal, or question:**

> It’s more about scaffeine behaviour, but I think it’s useful to capture this in a test
> 
> ‌
> 
> ```
> when(fxBrokerMock.createQuotation)
>   .thenReturn(_ => Future.failed(new Exception("some error")))
>   .thenReturn(_ => Future.successful(fxQuotation))
> ```
> 
> then make 2 calls to `getIndicativeFxQuotation` and verify the error is not cached, and that 2nd call will get successful response

**Conditions and limits:**

- Sequential mock first fails then succeeds; two getIndicativeFxQuotation calls should prove Scaffeine does not cache failures.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1558 · comment 479880342 · PR 8496 · 2024-03-08

Source path: `fxwallet-impl/src/test/scala/com/endowus/silver/fxwallet/impl/logic/service/FxWalletQuotationServiceImplSpec.scala`

**Evidence:** anon-2.jsonl:1558 · comment 479880342 · PR 8496 · 2024-03-08

Source path: `fxwallet-impl/src/test/scala/com/endowus/silver/fxwallet/impl/logic/service/FxWalletQuotationServiceImplSpec.scala`

**Explicit source context (pr_title):**

> TT-3906 New API to get cached indicative FX rates

## A2-1566 — TransactionJdbcProjectionV2: Let’s not mix the naming, it can be confusing for future readers:

**Source stance:** suggestion

**Context:**

> PR 8122 (Feat/INV-2203 clean up transaction old entities), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transactionV3/jdbc/TransactionJdbcProjectionV2.scala; original row 1566.

**Concern stated in the source:** Let’s not mix the naming, it can be confusing for future readers:

* `transaction-jdbc-handler-v1` is projection on V2 entity
* `transaction-jdbc-handler-v2` is projection on V3 entity to pipe data to V2

‌

I think let’s just use a bit more descriptive name to indicate that it’s projection from v3 entity to v2 repo. Maybe `transaction-v3-projection-to-v2-repo-v1`… last v1 is the version of the projection

Do same for the v1\_3 projection.

**Source-preserving request, proposal, or question:**

> Let’s not mix the naming, it can be confusing for future readers:
> 
> * `transaction-jdbc-handler-v1` is projection on V2 entity
> * `transaction-jdbc-handler-v2` is projection on V3 entity to pipe data to V2
> 
> ‌
> 
> I think let’s just use a bit more descriptive name to indicate that it’s projection from v3 entity to v2 repo. Maybe `transaction-v3-projection-to-v2-repo-v1`… last v1 is the version of the projection
> 
> Do same for the v1\_3 projection.

**Conditions and limits:**

- Projection source entity version and target repository version must be explicit; example transaction-v3-projection-to-v2-repo-v1 keeps last v1 as projection version.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1566 · comment 479020069 · PR 8122 · 2024-03-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transactionV3/jdbc/TransactionJdbcProjectionV2.scala`

**Evidence:** anon-2.jsonl:1566 · comment 479020069 · PR 8122 · 2024-03-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transactionV3/jdbc/TransactionJdbcProjectionV2.scala`

**Explicit source context (pr_title):**

> Feat/INV-2203 clean up transaction old entities

## A2-1606 — RebateDistributionCommunicationsManager: No need to sequence here? Just let `publishRebateDistributionPlatformNotifications` decide how to run its futures

**Source stance:** suggestion

**Context:**

> PR 8353 (Feat/INV-1996/automate trailer rebate), rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/managers/RebateDistributionCommunicationsManager.scala; original row 1606.

**Concern stated in the source:** No need to sequence here? Just let `publishRebateDistributionPlatformNotifications` decide how to run its futures

**Source-preserving request, proposal, or question:**

> No need to sequence here? Just let `publishRebateDistributionPlatformNotifications` decide how to run its futures

**Conditions and limits:**

- Caller need not Future.sequence if publishRebateDistributionPlatformNotifications owns concurrency.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1606 · comment 476108046 · PR 8353 · 2024-02-27

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/managers/RebateDistributionCommunicationsManager.scala`

**Evidence:** anon-2.jsonl:1606 · comment 476108046 · PR 8353 · 2024-02-27

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/managers/RebateDistributionCommunicationsManager.scala`

**Explicit source context (pr_title):**

> Feat/INV-1996/automate trailer rebate

## A2-1612 — RebateDistributionCommunicationsManager: Just Source and mapAsync these

**Source stance:** suggestion

**Context:**

> PR 8353 (Feat/INV-1996/automate trailer rebate), rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/managers/RebateDistributionCommunicationsManager.scala; original row 1612.

**Source-preserving request, proposal, or question:**

> Just Source and mapAsync these

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1612 · comment 476109463 · PR 8353 · 2024-02-27

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/managers/RebateDistributionCommunicationsManager.scala`

**Evidence:** anon-2.jsonl:1612 · comment 476109463 · PR 8353 · 2024-02-27

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/managers/RebateDistributionCommunicationsManager.scala`

**Explicit source context (hunk):**

> +          val mandatoryAltRebateInstruments = brokerRebates.flatMap(rebate => {
> +            altsRebatesMap
> +              .get(rebate.instrumentId)
> +              .flatMap(altsMandatoryRebate => instrumentMap.get(altsMandatoryRebate.instrumentId))
> +              .map { instrumentInfo =>
> +                MandatoryAltRebateInstrumentEmailView(
> +                  instrumentId = instrumentInfo.id,

**Evidence:** anon-2.jsonl:1612 · comment 476109463 · PR 8353 · 2024-02-27

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/managers/RebateDistributionCommunicationsManager.scala`

**Explicit source context (pr_title):**

> Feat/INV-1996/automate trailer rebate

## A2-1619 — RebateDistributionCommunicationsManager: Just Source the `customerRebates` and mapAsync to lookup instruments

**Source stance:** suggestion

**Context:**

> PR 8353 (Feat/INV-1996/automate trailer rebate), rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/managers/RebateDistributionCommunicationsManager.scala; original row 1619.

**Source-preserving request, proposal, or question:**

> Just Source the `customerRebates` and mapAsync to lookup instruments

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1619 · comment 478115107 · PR 8353 · 2024-03-04

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/managers/RebateDistributionCommunicationsManager.scala`

**Evidence:** anon-2.jsonl:1619 · comment 478115107 · PR 8353 · 2024-03-04

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/managers/RebateDistributionCommunicationsManager.scala`

**Explicit source context (pr_title):**

> Feat/INV-1996/automate trailer rebate

## A2-1638 — RegionalCustomerTopicCustomer: Entity is keyed by goalId so would it be better to increase parallelism for goals to 4, keeping parallelism for plans at 1?

**Source stance:** open-question

**Context:**

> PR 8215 ([INV-1959] feat(goal): Listen to customer deactivated msg), goal-impl/src/main/scala/com/endowus/silver/goal/impl/subscribers/RegionalCustomerTopicCustomer.scala; original row 1638.

**Concern stated in the source:** Entity is keyed by goalId so would it be better to increase parallelism for goals to 4, keeping parallelism for plans at 1?

**Source-preserving request, proposal, or question:**

> Entity is keyed by goalId so would it be better to increase parallelism for goals to 4, keeping parallelism for plans at 1?

**Conditions and limits:**

- Goal entity is keyed goalId; proposed goals parallelism=4 but plans within each goal=1.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1638 · comment 473482567 · PR 8215 · 2024-02-20

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/subscribers/RegionalCustomerTopicCustomer.scala`

**Evidence:** anon-2.jsonl:1638 · comment 473482567 · PR 8215 · 2024-02-20

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/subscribers/RegionalCustomerTopicCustomer.scala`

**Explicit source context (pr_title):**

> [INV-1959] feat(goal): Listen to customer deactivated msg

## A2-1649 — PreferredLocalLookupHelper: Can we add a base trait `PreferredLocalLookupHelper` too?

**Source stance:** suggestion

**Context:**

> PR 8242 ([EN-2895] feat(customer): PreferredLocalLookupHelper), customer-api/src/main/scala/com/endowus/silver/customer/api/commons/PreferredLocalLookupHelper.scala; original row 1649.

**Concern stated in the source:** Can we add a base trait `PreferredLocalLookupHelper` too?

```
trait PreferredLocalLookupHelper {
  def getPreferredLocale(customerId: UUID): Future[Locale]
}

trait SgPreferredLocalLookupHelper extends BaseHelper {
  def localConfig: LocalConfig
  final override def getPreferredLocale(customerId: UUID): Future[Locale] = ???
}

trait HkPreferredLocalLookupHelper extends BaseHelper {
  implicit def executionContext: ExecutionContext
  def regionalCustomerService: RegionalCustomerService
  final override def getPreferredLocale(customerId: UUID): Future[Locale] = ???
}
```

‌

This way we can use the base trait in those `Base*Projection` too

**Source-preserving request, proposal, or question:**

> Can we add a base trait `PreferredLocalLookupHelper` too?
> 
> ```
> trait PreferredLocalLookupHelper {
>   def getPreferredLocale(customerId: UUID): Future[Locale]
> }
> 
> trait SgPreferredLocalLookupHelper extends BaseHelper {
>   def localConfig: LocalConfig
>   final override def getPreferredLocale(customerId: UUID): Future[Locale] = ???
> }
> 
> trait HkPreferredLocalLookupHelper extends BaseHelper {
>   implicit def executionContext: ExecutionContext
>   def regionalCustomerService: RegionalCustomerService
>   final override def getPreferredLocale(customerId: UUID): Future[Locale] = ???
> }
> ```
> 
> ‌
> 
> This way we can use the base trait in those `Base*Projection` too

**Conditions and limits:**

- Base PreferredLocalLookupHelper enables shared Base*Projection use; SG and HK implementations retain their different dependencies.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1649 · comment 467668480 · PR 8242 · 2024-02-02

Source path: `customer-api/src/main/scala/com/endowus/silver/customer/api/commons/PreferredLocalLookupHelper.scala`

**Evidence:** anon-2.jsonl:1649 · comment 467668480 · PR 8242 · 2024-02-02

Source path: `customer-api/src/main/scala/com/endowus/silver/customer/api/commons/PreferredLocalLookupHelper.scala`

**Explicit source context (pr_title):**

> [EN-2895] feat(customer): PreferredLocalLookupHelper

## A2-1656 — enums: I think the industry terminology is advisory and execution-only? Also I’m not too sure about naming this `AdvisoryLevel`. I think there can a 3rd mode as well, aka discre...

**Source stance:** suggestion

**Context:**

> PR 8193 (Feat/INV-2101 execution advisory transaction tagging), silver-commons/src/main/scala/com/endowus/silver/commons/models/enums.scala; original row 1656.

**Concern stated in the source:** I think the industry terminology is advisory and execution-only? Also I’m not too sure about naming this `AdvisoryLevel`. I think there can a 3rd mode as well, aka discretionary? We don’t need to add this 3rd mode yet, but the enum name should allow it to be added in future

**Source-preserving request, proposal, or question:**

> I think the industry terminology is advisory and execution-only? Also I’m not too sure about naming this `AdvisoryLevel`. I think there can a 3rd mode as well, aka discretionary? We don’t need to add this 3rd mode yet, but the enum name should allow it to be added in future

**Conditions and limits:**

- Future discretionary classification should fit enum name, but adding discretionary mode now is explicitly unnecessary.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1656 · comment 465909080 · PR 8193 · 2024-01-29

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/models/enums.scala`

**Evidence:** anon-2.jsonl:1656 · comment 465909080 · PR 8193 · 2024-01-29

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/models/enums.scala`

**Explicit source context (pr_title):**

> Feat/INV-2101 execution advisory transaction tagging

## A2-1676 — AdvisoryDataTranslationManagerSpec: Maybe put the one needed for the test only. Now that we have the cache to mock, for readability, maybe use English instead :rofl: 

**Source stance:** suggestion

**Context:**

> PR 8161 (INV-2486: Add translation logic for fund smart templates.), advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/managers/AdvisoryDataTranslationManagerSpec.scala; original row 1676.

**Concern stated in the source:** Maybe put the one needed for the test only. Now that we have the cache to mock, for readability, maybe use English instead :rofl: 

I used the below instrument.. so in a way, I also assert the key lookup when validating the result

```
doAnswer { answer =>
  val translationKeys = answer.getArgument(0, classOf[Set[String]])
  Future.successful {
    translationKeys.map { key =>
      key -> key
    }.toMap
  }
}.when(instrumentTranslationCache).getCachedInstrumentTranslations(any(), any())
```

‌

**Source-preserving request, proposal, or question:**

> Maybe put the one needed for the test only. Now that we have the cache to mock, for readability, maybe use English instead :rofl: 
> 
> I used the below instrument.. so in a way, I also assert the key lookup when validating the result
> 
> ```
> doAnswer { answer =>
>   val translationKeys = answer.getArgument(0, classOf[Set[String]])
>   Future.successful {
>     translationKeys.map { key =>
>       key -> key
>     }.toMap
>   }
> }.when(instrumentTranslationCache).getCachedInstrumentTranslations(any(), any())
> ```
> 
> ‌

**Conditions and limits:**

- Test translation cache can echo key→key to assert lookup while keeping readable English fixtures.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1676 · comment 465896014 · PR 8161 · 2024-01-29

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/managers/AdvisoryDataTranslationManagerSpec.scala`

**Evidence:** anon-2.jsonl:1676 · comment 465896014 · PR 8161 · 2024-01-29

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/managers/AdvisoryDataTranslationManagerSpec.scala`

**Explicit source context (pr_title):**

> INV-2486: Add translation logic for fund smart templates.

## A2-1679 — RedemptionRequestTopicSubscriberV3: Let’s make this specific to fee redemption only, and move the `request.feeChargeDetails.isDefined` to require clause

**Source stance:** suggestion

**Context:**

> PR 8071 ([INV-1863] feat(transaction): Add cash reservation on assumed status for fee charge), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV3.scala; original row 1679.

**Concern stated in the source:** Let’s make this specific to fee redemption only, and move the `request.feeChargeDetails.isDefined` to require clause

Let’s not make assumption about single cash reservation. Today we support taking cash balance from single account, but in future we might not.

**Source-preserving request, proposal, or question:**

> Let’s make this specific to fee redemption only, and move the `request.feeChargeDetails.isDefined` to require clause
> 
> Let’s not make assumption about single cash reservation. Today we support taking cash balance from single account, but in future we might not.

**Conditions and limits:**

- Initial fee-only require proposal is corrected in row 1682 after realizing call also serves other flows. The warning against assuming one cash reservation still remains source-specific.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1679 · comment 463752982 · PR 8071 · 2024-01-23

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV3.scala`

**Evidence:** anon-2.jsonl:1679 · comment 463752982 · PR 8071 · 2024-01-23

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV3.scala`

**Explicit source context (pr_title):**

> [INV-1863] feat(transaction): Add cash reservation on assumed status for fee charge

## A2-1690 — PortfolioUnderlyingManager: Sorry [person]. I forgot we already have this fundDocuments → urlMap logic in FundDetails.toDto which takes care of returning latest version of these...

**Source stance:** suggestion

**Context:**

> PR 8020 ([INV-2498] feat(portfolio): enhance actual_asset_allocation with instrument v2 data), portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/managers/PortfolioUnderlyingManager.scala; original row 1690.

**Concern stated in the source:** Sorry [person]. I forgot we already have this fundDocuments → urlMap logic in FundDetails.toDto which takes care of returning latest version of these doc type.

Let’s revert back to use urlMap for now. In future, we can revisit this again, either replace these 3x string with full list of fundDocuments \(similar to fund details page\), or keep the 3x string and extract urlMap into a method of FundDetailsDto. We don’t know yet, let’s not worry about it for now :pray:

**Source-preserving request, proposal, or question:**

> Sorry [person]. I forgot we already have this fundDocuments → urlMap logic in FundDetails.toDto which takes care of returning latest version of these doc type.
> 
> Let’s revert back to use urlMap for now. In future, we can revisit this again, either replace these 3x string with full list of fundDocuments \(similar to fund details page\), or keep the 3x string and extract urlMap into a method of FundDetailsDto. We don’t know yet, let’s not worry about it for now :pray:

**Conditions and limits:**

- FundDetails.toDto already maps latest fundDocuments to urlMap. Revert now; full-list DTO or FundDetailsDto helper extraction are unresolved future alternatives.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1690 · comment 461165852 · PR 8020 · 2024-01-15

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/managers/PortfolioUnderlyingManager.scala`

> Sorry

**Evidence:** anon-2.jsonl:1690 · comment 461165852 · PR 8020 · 2024-01-15

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/managers/PortfolioUnderlyingManager.scala`

> . I forgot we already have this fundDocuments → urlMap logic in FundDetails.toDto which takes care of returning latest version of these doc type.
> 
> Let’s revert back to use urlMap for now. In future, we can revisit this again, either replace these 3x string with full list of fundDocuments \(similar to fund details page\), or keep the 3x string and extract urlMap into a method of FundDetailsDto. We don’t know yet, let’s not worry about it for now :pray:

**Evidence:** anon-2.jsonl:1690 · comment 461165852 · PR 8020 · 2024-01-15

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/managers/PortfolioUnderlyingManager.scala`

**Explicit source context (pr_title):**

> [INV-2498] feat(portfolio): enhance actual_asset_allocation with instrument v2 data

## A2-1712 — RebalanceApplication: Can you help to put a comment here to remind us about the mismatch between table version and readside version, to avoid future confusion :pray:

**Source stance:** suggestion

**Context:**

> PR 7899 (PLATFORM-1097: Rebalance service pg readside migration), rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/RebalanceApplication.scala; original row 1712.

**Source-preserving request, proposal, or question:**

> Can you help to put a comment here to remind us about the mismatch between table version and readside version, to avoid future confusion :pray:

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- Hunk example explicitly documents rebalance_plan_v2→projection v1, keeping independent table/projection versions.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1712 · comment 455418391 · PR 7899 · 2023-12-21

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/RebalanceApplication.scala`

**Evidence:** anon-2.jsonl:1712 · comment 455418391 · PR 7899 · 2023-12-21

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/RebalanceApplication.scala`

**Explicit source context (hunk):**

> +
> +    // NOTE: Projection version and table versions might differ. In this case, rebalance_plan_v2 -> projection v1
> +    val rebalancePlanJdbcProjection: RebalancePlanJdbcProjection =
> +      new RebalancePlanJdbcProjection(1, jdbcDatabase, jdbcDatabaseConfig, persistentEntityRefProvider, rebalancePlanJdbcRepository, dateTimeProvider)
> +    rebalancePlanJdbcProjection.start()
> +    val auroraRebalancePlanJdbcProjection: RebalancePlanJdbcProjection =
> +      new RebalancePlanJdbcProjection(2, auroraJdbcDatabase, auroraJdbcDatabaseConfig, persistentEntityRefProvider, auroraRebalancePlanJdbcRepository, dateTimeProvider)

**Evidence:** anon-2.jsonl:1712 · comment 455418391 · PR 7899 · 2023-12-21

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/RebalanceApplication.scala`

**Explicit source context (pr_title):**

> PLATFORM-1097: Rebalance service pg readside migration

## A2-1731 — SgFundSmartManagerV3: At this point we don’t have any remote calls anymore, can do mapAsync\(4\) I think

**Source stance:** suggestion

**Context:**

> PR 7719 (Resolve INV-2348: support bulk look up of performance), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgFundSmartManagerV3.scala; original row 1731.

**Source-preserving request, proposal, or question:**

> At this point we don’t have any remote calls anymore, can do mapAsync\(4\) I think

**Conditions and limits:**

- mapAsync(4) suggestion applies after no remote calls remain, distinct from ordered Kafka subscriber parallelism limits.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1731 · comment 451514621 · PR 7719 · 2023-12-07

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgFundSmartManagerV3.scala`

**Evidence:** anon-2.jsonl:1731 · comment 451514621 · PR 7719 · 2023-12-07

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgFundSmartManagerV3.scala`

**Explicit source context (pr_title):**

> Resolve INV-2348: support bulk look up of performance

## A2-1733 — SgFundSmartManagerV3: Yeah `performanceMap` already contains only that specific period type \(if any\)

**Source stance:** suggestion

**Context:**

> PR 7719 (Resolve INV-2348: support bulk look up of performance), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgFundSmartManagerV3.scala; original row 1733.

**Concern stated in the source:** Yeah `performanceMap` already contains only that specific period type \(if any\)

```
val commonPerformancesFut = instrumentPerformanceCache.getCachedInstrumentPerformances(instrumentCcyMap, COMMON)
val fundInceptionPerformancesFut = instrumentPerformanceCache.getCachedInstrumentPerformances(instrumentCcyMap, FUND_INCEPTION)
....
lazy val commonPeriodPerformanceFut = createFuture(instrument.id, COMMON, commonPerformances)
lazy val fundInceptionPerformanceFut = createFuture(instrument.id, FUND_INCEPTION, fundInceptionPerformances)
```

‌

**Source-preserving request, proposal, or question:**

> Yeah `performanceMap` already contains only that specific period type \(if any\)
> 
> ```
> val commonPerformancesFut = instrumentPerformanceCache.getCachedInstrumentPerformances(instrumentCcyMap, COMMON)
> val fundInceptionPerformancesFut = instrumentPerformanceCache.getCachedInstrumentPerformances(instrumentCcyMap, FUND_INCEPTION)
> ....
> lazy val commonPeriodPerformanceFut = createFuture(instrument.id, COMMON, commonPerformances)
> lazy val fundInceptionPerformanceFut = createFuture(instrument.id, FUND_INCEPTION, fundInceptionPerformances)
> ```
> 
> ‌

**Conditions and limits:**

- Common/fund-inception performance Maps are already scoped by period type; lazy per-instrument Future lookup need not check cross-period data.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1733 · comment 452604255 · PR 7719 · 2023-12-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgFundSmartManagerV3.scala`

**Evidence:** anon-2.jsonl:1733 · comment 452604255 · PR 7719 · 2023-12-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgFundSmartManagerV3.scala`

**Explicit source context (pr_title):**

> Resolve INV-2348: support bulk look up of performance

## A2-1784 — HkFundSmartTemplateRecommendedLabelHelper: It’s all hard-coded, we can make these 2 Maps `lazy val` instead

**Source stance:** suggestion

**Context:**

> PR 7629 ([EN-2548] Add recommended label to getRecommendedFundSmartTemplates), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/fundsmart/hk/HkFundSmartTemplateRecommendedLabelHelper.scala; original row 1784.

**Source-preserving request, proposal, or question:**

> It’s all hard-coded, we can make these 2 Maps `lazy val` instead

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1784 · comment 447866720 · PR 7629 · 2023-11-27

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/fundsmart/hk/HkFundSmartTemplateRecommendedLabelHelper.scala`

**Evidence:** anon-2.jsonl:1784 · comment 447866720 · PR 7629 · 2023-11-27

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/fundsmart/hk/HkFundSmartTemplateRecommendedLabelHelper.scala`

**Explicit source context (pr_title):**

> [EN-2548] Add recommended label to getRecommendedFundSmartTemplates

## A2-1788 — InstrumentDataUpdateManagerV2: Maybe move this up so we fail faster. Also need to `throw` instead of `Future.failed` if using `=`, i.e. `Future#map`

**Source stance:** suggestion

**Context:**

> PR 7611 (Resolve INV-1796: New wealth sync/MStar on-demand sync), instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentDataUpdateManagerV2.scala; original row 1788.

**Concern stated in the source:** Maybe move this up so we fail faster. Also need to `throw` instead of `Future.failed` if using `=`, i.e. `Future#map`

‌

**Source-preserving request, proposal, or question:**

> Maybe move this up so we fail faster. Also need to `throw` instead of `Future.failed` if using `=`, i.e. `Future#map`
> 
> ‌

**Conditions and limits:**

- Map binding `_ =` must throw; Future.failed would merely return failed Future as ignored value. Move cheap validation earlier.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1788 · comment 447872697 · PR 7611 · 2023-11-27

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentDataUpdateManagerV2.scala`

**Evidence:** anon-2.jsonl:1788 · comment 447872697 · PR 7611 · 2023-11-27

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentDataUpdateManagerV2.scala`

**Explicit source context (pr_title):**

> Resolve INV-1796: New wealth sync/MStar on-demand sync

## A3-0003 — MStar sync Futures: retry, current-DB fallback and final-error logging

**Source stance:** suggestion

**Context:**

> marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; PR: Feat/INV-2229 marketdata ex dividend bond yield

**Source-preserving request, proposal, or question:**

> Each fut might fail, so maybe we get current data in db and use that as fallback if call to MStar \(with retries\) fails? Log error when we give up on retry

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1809 · comment 442779203 · PR 7443 · 2023-11-08

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Evidence:** anon-2.jsonl:1809 · comment 442779203 · PR 7443 · 2023-11-08

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (hunk):**

> +  private def innerSyncInstrumentMstarData(instrumentInfoDto: InstrumentInfoDto): Future[Done] = {
> +    val instrumentId = instrumentInfoDto.id
> +    val instrumentCcy = instrumentInfoDto.priceCcy
> +
> +    logger.info(s"innerSyncInstrumentMstarData started for instrument [$instrumentId][$instrumentCcy]")
> +
> +    def yieldToMaturityFut(id: MstarApiId, existingData: Option[BigDecimal]): Future[Option[BigDecimal]] =

## A3-0010 — ServiceLogicImpl.scala: Does this look better? ``` instrumentId .map(marketDataUploader.syncInstrumentMstarData) .getOrElse { // run in background marketDataUploader.safeSync

**Source stance:** suggestion

**Context:**

> marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala; PR: Feat/INV-2229 marketdata ex dividend bond yield

**Source-preserving request, proposal, or question:**

> Does this look better?
> 
> ```
> instrumentId
>   .map(marketDataUploader.syncInstrumentMstarData)
>   .getOrElse {
>       // run in background
>       marketDataUploader.safeSyncInstrumentMstarData()
>       Future.successful(Done)
>   }
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1816 · comment 442802096 · PR 7443 · 2023-11-08

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

> Does this look better?
> 
> ```
> instrumentId
>   .map(marketDataUploader.syncInstrumentMstarData)
>   .getOrElse {
>       // run in background
>       marketDataUploader.safeSyncInstrumentMstarData()
>       Future.successful(Done)
>   }
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:1816 · comment 442802096 · PR 7443 · 2023-11-08

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +    }}
> +  }
> +
> +  override def getInstrumentMstarData(instrumentId: String): Future[Option[InstrumentMstarDataDto]] = {
> +    for {
> +      maybeInstrumentData <- instrumentMStarDataRepository.findByInstrumentId(instrumentId)
> +    } yield maybeInstrumentData.map(InstrumentMstarData.toDto)

## A3-0018 — MAS getLatest on weekend/currency holiday: latest available rate and optional tail recursion

**Source stance:** requested-change

**Context:**

> marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/mas/MasApiServiceV2.scala; PR: Resolve INV-2241: Add new api facade for migrated MAS eod fx api.

**Source-preserving request, proposal, or question:**

> Yup we don’t have rates during weekend or potentially ccy holiday. getLatest api should just return latest available, rather than throwing.
> 
> It’s all local to this class, so you can even just return Optional \(with some logging\) and we can tailrec

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1826 · comment 441115260 · PR 7360 · 2023-11-02

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/mas/MasApiServiceV2.scala`

**Evidence:** anon-2.jsonl:1826 · comment 441115260 · PR 7360 · 2023-11-02

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/mas/MasApiServiceV2.scala`

**Explicit source context (hunk):**

> +    def retrieveForDateAndRetroactively(ccy: CurrencyUnit, fxDate: LocalDate, reverse: Boolean): Future[(LocalDate, BigDecimal)] = {
> +      for {
> +        fxRate <- getFxRateAgainstSGDFromMasApi(ccy, fxDate, reverse)
> +        result <- if (fxRate.isDefined) {
> +          Future.successful(fxRate.get)
> +        } else {
> +          val nextDateToCheck = fxDate.minusDays(1)

## A3-0026 — InstrumentV2JdbcDbHandler.scala: We don’t really need transaction for readside so we can inject db here, and return Future… it’s easier to use and mock in test if needed

**Source stance:** suggestion

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/db/jdbc/InstrumentV2JdbcDbHandler.scala; PR: Resolve INV-2127: New read side table instrument entity v2

**Source-preserving request, proposal, or question:**

> We don’t really need transaction for readside so we can inject db here, and return Future… it’s easier to use and mock in test if needed

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1834 · comment 439499719 · PR 7211 · 2023-10-27

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/db/jdbc/InstrumentV2JdbcDbHandler.scala`

**Evidence:** anon-2.jsonl:1834 · comment 439499719 · PR 7211 · 2023-10-27

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/db/jdbc/InstrumentV2JdbcDbHandler.scala`

**Explicit source context (hunk):**

> +  private val instruments = TableQuery[InstrumentV2Table]
> +
> +  def upsert(instrument: Instrument): Future[Unit] = {
> +    db.run(instruments.insertOrUpdate(instrument)).flatMap {
> +      case 0 | 1 => Future.unit
> +      case n     => Future.failed(new Exception(s"Expected 0 or 1 updated, but got $n"))
> +    }

## A3-0044 — ComplianceServiceException NotFound caught for unrelated scenario causes unnecessary retries

**Source stance:** observed-defect

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImpl.scala; PR: [ONB-2877] feature(advisory): Added a retry mechanism for CKA checks during SG goal summary creation

**Source-preserving request, proposal, or question:**

> This guy throws `ComplianceServiceException` NotFound but has nothing to do with the scenario you’re handling… so now this method will unnecessarily retry

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1855 · comment 439504832 · PR 7314 · 2023-10-27

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:1855 · comment 439504832 · PR 7314 · 2023-10-27

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImpl.scala`

**Explicit source context (hunk):**

> }
>    }
>    override def computeRetailCustomerCkaStatus(customerId: UUID): Future[CustomerKnowledgeAssessmentStatus] = {
> -    if (IsComplianceCheckEnabledGlobally) {
> -      val customerFut = customerService.getCustomerV2(customerId).invoke()
> -
> +    if (!IsComplianceCheckEnabledGlobally) {
> +      Future.successful(CustomerKnowledgeAssessmentStatus.Valid)
> +    } else {
>        for {
> -        customer <- customerFut
> -        maybeCka <- customerKnowledgeAssessmentRepository.getByCustomerId(customerId)
> +        customer <- customerService.getCustomerV2(customerId).invoke()
>          maybeIsAi = customer.singaporeSpecificDetails.map(_.isAi)
> -        isAi = maybeIsAi.contains(true)
> -        statu

## A3-0045 — ServiceLogicImpl.scala: advisory circuit breaker timeout will kick in at 15s… do we need this long?

**Source stance:** open-question

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImpl.scala; PR: [ONB-2877] feature(advisory): Added a retry mechanism for CKA checks during SG goal summary creation

**Source-preserving request, proposal, or question:**

> advisory circuit breaker timeout will kick in at 15s… do we need this long?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1856 · comment 439505187 · PR 7314 · 2023-10-27

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:1856 · comment 439505187 · PR 7314 · 2023-10-27

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +              logger.info(s"Skip retrying computeCkaStatusFut, customerId: ${customerId}")
> +              false
> +          },
> +          settings = sgComplianceServiceRetrySettings.calculateCkaStatusRetrySettings,
> +          context = "computeRetailCustomerCkaStatusWithRetryIfNotFound retry"
> +        )
> +        .recoverWith {

## A3-0046 — compliance-slowProcess identifies compliance circuit breaker and uses slowProcess config

**Source stance:** requested-change

**Context:**

> compliance-api/src/main/scala/com/endowus/silver/compliance/api/ComplianceService.scala; PR: [ONB-2877] feature(advisory): Added a retry mechanism for CKA checks during SG goal summary creation

**Concern stated in the source:** This should be `compliance-slowProcess` cuz it’s circuit breaker id for compliance svc.

**Source-preserving request, proposal, or question:**

> This should be `compliance-slowProcess` cuz it’s circuit breaker id for compliance svc.
> 
> We then can use default slowProcess config for it in `lagom-circuit-breaker.conf`

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1859 · comment 439574141 · PR 7314 · 2023-10-27

Source path: `compliance-api/src/main/scala/com/endowus/silver/compliance/api/ComplianceService.scala`

**Evidence:** anon-2.jsonl:1859 · comment 439574141 · PR 7314 · 2023-10-27

Source path: `compliance-api/src/main/scala/com/endowus/silver/compliance/api/ComplianceService.scala`

**Explicit source context (hunk):**

> //CKA
> -        restCall(Method.GET, "/api/v1/general-customer-knowledge-assessment/:customerId/status", computeGeneralCustomerCkaStatus _),
> +        restCall(Method.GET, "/api/v1/general-customer-knowledge-assessment/:customerId/status", computeGeneralCustomerCkaStatus _).withCircuitBreaker(
> +          CircuitBreaker.identifiedBy("compliance-slowProcess")
> +        ),
>          // CKA Status with recurring
>          restCall(

## A3-0047 — ServiceLogicImpl.scala: recoverWith expects a Future as return type so you can use Future.failed\(ex\) instead

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImpl.scala; PR: [ONB-2877] feature(advisory): Added a retry mechanism for CKA checks during SG goal summary creation

**Source-preserving request, proposal, or question:**

> recoverWith expects a Future as return type so you can use Future.failed\(ex\) instead

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:1860 · comment 439577565 · PR 7314 · 2023-10-27

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImpl.scala`

## A3-0048 — Compliance retry test: trust FutureUtils or override backoff for short unit tests

**Source stance:** suggestion

**Context:**

> compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImplTest.scala; PR: [ONB-2877] feature(advisory): Added a retry mechanism for CKA checks during SG goal summary creation

**Concern stated in the source:** Otherwise you should provide a way to override the retry settings to make it way shorter in a unit test

**Source-preserving request, proposal, or question:**

> This will be very slow test… in compliance svc code, you can trust the behaviour of `FutureUtils.futureWithRetry`… no need to add this test I think.
> 
> Otherwise you should provide a way to override the retry settings to make it way shorter in a unit test

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1861 · comment 439578348 · PR 7314 · 2023-10-27

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImplTest.scala`

> This will be very slow test… in compliance svc code, you can trust the behaviour of `FutureUtils.futureWithRetry`… no need to add this test I think.
> 
> Otherwise you should provide a way to override the retry settings to make it way shorter in a unit test
> 
> ‌

**Evidence:** anon-2.jsonl:1861 · comment 439578348 · PR 7314 · 2023-10-27

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImplTest.scala`

**Explicit source context (hunk):**

> +        }.map { _ =>
> +          verify(customerService, times(1)).getCustomerV2(mockRegionalCustomerDto.customerId)
> +          // 1 invocation with 5 retries
> +          verify(customerKnowledgeAssessmentRepository, times(6)).getByCustomerId(mockRegionalCustomerDto.customerId)
> +          succeed
> +        }
> +      }

## A3-0055 — PortfolioOfferingResponseV2 sealed-trait concern and product-specific MAA card flow

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgAdvisedPortfolioMaaManager.scala; PR: Feat/INV-634/migrate refactor maa endpoints

**Source-preserving request, proposal, or question:**

> Not sure if it’s worth adding this sealed trait `PortfolioOfferingResponseV2` just for this purpose or not. We also go against the common pattern of sealed trait, in which we just use it for pattern matching, but data sent back in endpoints is still specific type.
> 
> 
> 
> I feel splitting code like below is still ok
> 
> ```
> def getMaaCards(productLine, tradingAccountType, displayCcy) = {
>   productLine match {
>     case Flagship => getFlagshipMaaCards(tradingAccountType, displayCcy)
>     ...
>   }
> }
> 
> def getFlagshipMaaCards(tradingAccountType, displayCcy) = {
>   for {
>     portfolioOfferings <- getFlagshipOfferings(Some(accountType))
>     cards <- Source(portfolioOfferings.toList)
>       .mapAsync(2) { portfolioOffering =>
>         maaAdditionalDetailsCache.get(portfolioOffering.portfolioId, portfolioOffering.effectiveDate, displayCcy)
>           .map { case (performance, composition) =>
>             PortfolioMaaCard.fromFlagshipPortfolioOffering(...)
>           }
>       }
>       .runWith(Sink.seq)
>       .map(_.toList)
>   } yields cards
> }
> 
> def getEsgMaaCards / getIncomeMaaCards / etc.
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1868 · comment 438181785 · PR 7274 · 2023-10-23

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgAdvisedPortfolioMaaManager.scala`

> Not sure if it’s worth adding this sealed trait `PortfolioOfferingResponseV2` just for this purpose or not. We also go against the common pattern of sealed trait, in which we just use it for pattern matching, but data sent back in endpoints is still specific type.
> 
> ‌
> 
> I feel splitting code like below is still ok
> 
> ```
> def getMaaCards(productLine, tradingAccountType, displayCcy) = {
>   productLine match {
>     case Flagship => getFlagshipMaaCards(tradingAccountType, displayCcy)
>     ...
>   }
> }
> 
> def getFlagshipMaaCards(tradingAccountType, displayCcy) = {
>   for {
>     portfolioOfferings <- getFlagshipOfferings(Some(accountType))
>     cards <- Source(portfolioOfferings.toList)
>       .mapAsync(2) { portfolioOffering =>
>         maaAdditionalDetailsCache.get(portfolioOffering.portfolioId, portfolioOffering.effectiveDate, displayCcy)
>           .map { case (performance, composition) =>
>             PortfolioMaaCard.fromFlagshipPortfolioOffering(...)
>           }
>       }
>       .runWith(Sink.seq)
>       .map(_.toList)
>   } yields cards
> }
> 
> def getEsgMaaCards / getIncomeMaaCards / etc.
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:1868 · comment 438181785 · PR 7274 · 2023-10-23

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgAdvisedPortfolioMaaManager.scala`

**Explicit source context (hunk):**

> +            response = portfolioOffering,
> +            underlyingPage = underlyingPage,
> +            performance = performance,
> +            displayCcy = displayCcy
> +          )
> +        }
> +        }.runWith(Sink.seq).map(s => s.toList)

## A3-0062 — InvestmentRequestTopicSubscriberV3.scala: Should be able to remove this throttle?

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/InvestmentRequestTopicSubscriberV3.scala; PR: Feat/INV-1972 v3 transaction subscriber

**Source-preserving request, proposal, or question:**

> Should be able to remove this throttle?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1877 · comment 439569394 · PR 7303 · 2023-10-27

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/InvestmentRequestTopicSubscriberV3.scala`

**Evidence:** anon-2.jsonl:1877 · comment 439569394 · PR 7303 · 2023-10-27

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/InvestmentRequestTopicSubscriberV3.scala`

**Explicit source context (hunk):**

> +    .subscribe
> +    .withGroupId(groupId)
> +    .atLeastOnce(Flow[InvestmentRequestMsg]
> +    .mapAsync(parallelism = 1) {
> +      case msg: InvestmentRequestedMsg if isNotDividendReinvestment(msg.request.reason) =>
> +        val request = msg.request
> +        logMessage(msg, request.investmentRequestId)

## A3-0071 — ServiceLogicImplV2.scala: This one is old code, but I think better to mapAsync so that we can control the parallelism instead of blind run with throttle… we can ignore the resu

**Source stance:** suggestion

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/impl/ServiceLogicImplV2.scala; PR: Resolve INV-2049: New instrument events, event handlers, v2 logic split.

**Concern stated in the source:** This one is old code, but I think better to mapAsync so that we can control the parallelism instead of blind run with throttle… we can ignore the result Future easily afterwards

**Source-preserving request, proposal, or question:**

> This one is old code, but I think better to mapAsync so that we can control the parallelism instead of blind run with throttle… we can ignore the result Future easily afterwards

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1887 · comment 437292455 · PR 7097 · 2023-10-19

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/impl/ServiceLogicImplV2.scala`

**Evidence:** anon-2.jsonl:1887 · comment 437292455 · PR 7097 · 2023-10-19

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/impl/ServiceLogicImplV2.scala`

**Explicit source context (hunk):**

> +
> +      // Fire and forget as caller doesn't need to wait for everything to be successful
> +      _ <- Source(instruments)
> +        .throttle(2, 250.millisecond, 1, ThrottleMode.Shaping)
> +        .mapAsync(parallelism = 1) { instrument =>
> +          instrumentEntity.ref(instrument.id).ask(PublishInstrumentCmd(_))
> +        }

## A3-0072 — InstrumentDataUpdateManagerV2.scala: no need for comprehend if just single future

**Source stance:** suggestion

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentDataUpdateManagerV2.scala; PR: Resolve INV-2049: New instrument events, event handlers, v2 logic split.

**Source-preserving request, proposal, or question:**

> Nit: no need for comprehend if just single future

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1888 · comment 437293213 · PR 7097 · 2023-10-19

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentDataUpdateManagerV2.scala`

**Evidence:** anon-2.jsonl:1888 · comment 437293213 · PR 7097 · 2023-10-19

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentDataUpdateManagerV2.scala`

**Explicit source context (hunk):**

> +
> +  def instrumentEntity: InstrumentV2Entity
> +  def dateTimeProvider: DateTimeProvider
> +  def instrumentJdbcRepository: InstrumentV2JdbcRepository
> +  def mstarApiService: MstarApiService
> +
> +  override def addInstrumentId(request: commons.AddInstrumentIdRequest): Future[InstrumentInfoDto] = {

## A3-0107 — Quarterly fee estimate avoids Kafka task: no OOMKilled and idle partition/consumer cost

**Source stance:** explanation

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/FeeEstimateNotificationManager.scala; PR: [INV-2016] feat(communication)(charge): Email notification for estimated upcoming quarterly charge (support only NonAlts for now)

**Source-preserving request, proposal, or question:**

> Not using Kafka task for this, for now:
> 
> * we don’t have OOMKilled problem, and this process should be fast to complete
> * we only have this exercise once a quarter, so it’s wasteful to have kafka topic created \(charged per partitions\) and idle kafka consumers

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1924 · comment 433289502 · PR 7106 · 2023-10-05

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/FeeEstimateNotificationManager.scala`

> Not using Kafka task for this, for now:
> 
> * we don’t have OOMKilled problem, and this process should be fast to complete
> * we only have this exercise once a quarter, so it’s wasteful to have kafka topic created \(charged per partitions\) and idle kafka consumers
> 
> ‌

**Evidence:** anon-2.jsonl:1924 · comment 433289502 · PR 7106 · 2023-10-05

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/FeeEstimateNotificationManager.scala`

**Explicit source context (hunk):**

> +          chargeDate = chargeDate,
> +          forceResend = request.forceResend
> +        )
> +        sendCustomerFeeEstimateNotification(customerRequest, simulateOnly = None)
> +          .map(_ => Right(Done))
> +          .recover {
> +            case ex =>

## A3-0115 — ServiceLogicImpl.scala: ~~Actually the common code should be a method that takes List\[GoalDto\] and return Future\[List\[RecommendedPortfolioChangeDto\]\]~~ ~~Then customer 

**Source stance:** suggestion

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala; PR: [INV-1988] feat(gateway, rebalance): migrate recommended portfolio changes endpoint from davinci

**Source-preserving request, proposal, or question:**

> ~~Actually the common code should be a method that takes List\[GoalDto\] and return Future\[List\[RecommendedPortfolioChangeDto\]\]~~
> 
> ~~Then customer endpoint pass in all active goals, while goal endpoint pass in exactly one goal~~

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- The entire suggestion is struck through in the source; do not present as a live requirement.
- Related source rows 1932, 1933: Struck-through shared-code suggestion is revised to explain customer-readside versus goal-entity behavior.

**Evidence:** anon-2.jsonl:1932 · comment 431718346 · PR 6874 · 2023-09-29

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:1932 · comment 431718346 · PR 6874 · 2023-09-29

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +      plans = goal.plans.map(p => (p.planId, p.tradingAccountType, goal.name, goal.investmentGoalType))
> +      recommendedPortfolioChangeDtos <- Source(plans)
> +        .mapAsync(2) {
> +          case (planId, tradingAccountType, goalName, goalType) =>
> +            for {
> +              rebalanceRequestDtos <- getRebalanceRequestDtosForGoal(
> +                customerId = goal.customerId,

## A3-0124 — ServiceLogicImpl.scala: We have utils in OptionUtils so this can be written as ``` rpcCmsWebflowIdJdbcRepository .find(portfolioId, effectiveDate) .map(_.map { entry => RpcCm

**Source stance:** suggestion

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala; PR: Feat/INV-1986/rpc-communication-details-crud

**Source-preserving request, proposal, or question:**

> We have utils in OptionUtils so this can be written as
> 
> ```
> rpcCmsWebflowIdJdbcRepository
>   .find(portfolioId, effectiveDate)
>   .map(_.map { entry =>
>     RpcCmsWebflowIdEntryDto(
>       portfolioId = entry.portfolioId,
>       effectiveDate = entry.effectiveDate,
>       collectionId = entry.collectionId,
>       itemId = entry.itemId,
>       description = entry.description,
>       updatedAt = entry.updatedAt
>     )
>   }.onNone(logger.warn(...)))
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:1942 · comment 429926815 · PR 6989 · 2023-09-22

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala`

> We have utils in OptionUtils so this can be written as
> 
> ```
> rpcCmsWebflowIdJdbcRepository
>   .find(portfolioId, effectiveDate)
>   .map(_.map { entry =>
>     RpcCmsWebflowIdEntryDto(
>       portfolioId = entry.portfolioId,
>       effectiveDate = entry.effectiveDate,
>       collectionId = entry.collectionId,
>       itemId = entry.itemId,
>       description = entry.description,
>       updatedAt = entry.updatedAt
>     )
>   }.onNone(logger.warn(...)))
> ```
> 
> ‌

## A3-0125 — ServiceLogicImpl.scala: Same here, you don’t need to match. Can extract to reuse same toDto method as well ``` rpcCmsWebflowIdJdbcRepository .findByItemId(itemId) .map(_.map(

**Source stance:** suggestion

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala; PR: Feat/INV-1986/rpc-communication-details-crud

**Source-preserving request, proposal, or question:**

> Same here, you don’t need to match. Can extract to reuse same toDto method as well
> 
> ```
> rpcCmsWebflowIdJdbcRepository
>   .findByItemId(itemId)
>   .map(_.map(toDto))
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:1943 · comment 429927351 · PR 6989 · 2023-09-22

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala`

> Same here, you don’t need to match. Can extract to reuse same toDto method as well
> 
> ```
> rpcCmsWebflowIdJdbcRepository
>   .findByItemId(itemId)
>   .map(_.map(toDto))
> ```
> 
> ‌

## A3-0143 — BaseChargeService.scala: It’s too heavy to run for all customers even for Alts. So I revert back to expecting for single customerId

**Source stance:** explanation

**Context:**

> charge-api/src/main/scala/com/endowus/silver/charge/api/BaseChargeService.scala; PR: [INV-2014] feat(voucher)(charge): Support discount + tax simulation in fee query endpoint

**Source-preserving request, proposal, or question:**

> It’s too heavy to run for all customers even for Alts. So I revert back to expecting for single customerId

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1961 · comment 431721258 · PR 7042 · 2023-09-29

Source path: `charge-api/src/main/scala/com/endowus/silver/charge/api/BaseChargeService.scala`

**Evidence:** anon-2.jsonl:1961 · comment 431721258 · PR 7042 · 2023-09-29

Source path: `charge-api/src/main/scala/com/endowus/silver/charge/api/BaseChargeService.scala`

**Explicit source context (hunk):**

> ): ServiceCall[NotUsed, FeeEstimationResponse]
>  
> -  def queryPlanFees(customerId: Option[UUID], year: Int, quarter: String, queryType: String): ServiceCall[NotUsed, FeeQueryResponse]
> +  def queryPlanFees(customerId: UUID, year: Int, quarter: String, queryType: String): ServiceCall[NotUsed, FeeQueryResponse]
>  
>    def getAltsMandatoryRebates: ServiceCall[NotUsed, List[AltsMandatoryRebateDto]]

## A3-0150 — Voucher wallet calculation needs full GetVoucherWalletStateCmd; entity load is bottleneck

**Source stance:** explanation

**Context:**

> voucher-impl/src/main/scala/com/endowus/silver/voucher/impl/entities/voucherWallet/VoucherWalletEntity.scala; PR: [INV-2014] feat(voucher)(charge): Support discount + tax simulation in fee query endpoint

**Source-preserving request, proposal, or question:**

> Ah we don’t have existing adequate readside for this. Will need to return whole state via `GetVoucherWalletStateCmd` to perform this calculation outside.
> 
> However, calculation itself is very simple, and in memory. The bottleneck would still be loading the entity itself.
> 
> Plus, we do this at customer level, not at plan level, so I think should be ok.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1969 · comment 432267560 · PR 7042 · 2023-10-02

Source path: `voucher-impl/src/main/scala/com/endowus/silver/voucher/impl/entities/voucherWallet/VoucherWalletEntity.scala`

**Evidence:** anon-2.jsonl:1969 · comment 432267560 · PR 7042 · 2023-10-02

Source path: `voucher-impl/src/main/scala/com/endowus/silver/voucher/impl/entities/voucherWallet/VoucherWalletEntity.scala`

**Explicit source context (hunk):**

> +    Effect.persist[Event, State](events.toList).thenAck(cmd.replyTo)
> +  }
> +
> +  def handleSimulateDiscountCmd(entityId: EntityId, cmd: SimulateDiscountCmd, state: VoucherWalletState): Persist = {
> +    if (state.rewardedVouchers.isEmpty || cmd.requests.isEmpty) {
> +      return Effect.replySuccess(cmd.replyTo)(SimulatedDiscounts(List()))
> +    }

## A3-0198 — CustomerTransactionMigrationEventProcessor.scala: You can `import com.endowus.silver.commons.utils.FutureUtils.FutureRetryExt` And use it like this ``` fut.withRetry(AlwaysRetryOnException) ```

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/customer/processors/CustomerTransactionMigrationEventProcessor.scala; PR: Feat/INV-1972 transaction migrator processor

**Source-preserving request, proposal, or question:**

> You can `import com.endowus.silver.commons.utils.FutureUtils.FutureRetryExt`
> 
> And use it like this
> 
> ```
> fut.withRetry(AlwaysRetryOnException)
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2019 · comment 427007327 · PR 6863 · 2023-09-13

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/customer/processors/CustomerTransactionMigrationEventProcessor.scala`

> You can `import com.endowus.silver.commons.utils.FutureUtils.FutureRetryExt`
> 
> And use it like this
> 
> ```
> fut.withRetry(AlwaysRetryOnException)
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2019 · comment 427007327 · PR 6863 · 2023-09-13

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/customer/processors/CustomerTransactionMigrationEventProcessor.scala`

**Explicit source context (hunk):**

> +    val eventTimestamp = ZonedDateTime.ofInstant(Instant.ofEpochMilli(ele.timestamp), dateTimeProvider.zoneId)
> +
> +    val updateTransactionFut = for {
> +      transactionV2 <- convertTransaction(transaction, eventTimestamp)
> +      //We force update for backfill events (e.g feeCharge TaxAbsorbed backfill), since it already reached terminal status
> +      res <- refProvider.getTransactionEntityRef(transaction.transactionId)
> +        .ask(UpdateTransactionCmd(_, transactionV2, forceUpdate = true))

## A3-0218 — Lagom/removed-Lagom error-serdes, shared breaker, whitelist and request-timeout verification matrix

**Source stance:** reported-verification

**Context:**

> None; PR: [INV-1974] feat(all-services): Consolidate svc exception serdes + circuit breaker config

**Concern stated in the source:** Able to return custom error json \(so that other services can deserialize\) instead of the default text response.

**Source-preserving request, proposal, or question:**

> ## Test setup
> 
> instrument svc: Lagom-removed with test endpoint
> 
> * serialize error using ServiceErrorCompat
> * its client services deserialize error using `LagomCompatServiceExceptionSerializer`
> 
> ```
>   def testWater(testType: String): Future[Done] = {
>     testType match {
>       case "LagomBadRequest"  => Future.failed(lagomBadRequest("Invalid request"))
>       case "EndowusNotFound"  => Future.failed(apiNotFound("Entity id not found"))
>       case "SvcException"     => Future.failed(InstrumentSvcException("MorningStar down!", InstrumentSvcErrorType.MORNINGSTAR_API_CALL_FAILURE))
>       case "RuntimeException" => Future { Option.empty.get }
>       case "Slow"             => Future { Thread.sleep(20000) }.map(_ => Done)
>       case _                  => Future.successful(Done)
>     }
>   }
> ```
> 
> ```
> restCall(Method.GET, "/api/internal/instrument/test-water?testType", testWater _)
>     .withCircuitBreaker(CircuitBreaker.identifiedBy("shared-testing")),
> ```
> 
>  
> 
> marketdata svc: Lagom with test endpoint
> 
> * serialize error using `LagomServiceExceptionSerializer`
> * its client services also deserialize error using `LagomServiceExceptionSerializer`
> 
> ```
>   override def testWater(testType: String): ServiceCall[NotUsed, Done] = ServiceCall { _ =>
>     testType match {
>       case "LagomBadRequest"  => Future.failed(BadRequest("Invalid request"))
>       case "EndowusNotFound"  => Future.failed(NotFound("Entity id not found"))
>       case "SvcException"     => Future.failed(MarketDataSvcException("MAS down!", MarketDataSvcErrorType.MAS_MAINTENANCE))
>       case "RuntimeException" => Future { List.empty(1) }
>       case "Slow"             => Future { Thread.sleep(20000) }.map(_ => Done)
>       case _                  => Future.successful(Done)
>     }
>   }
> ```
> 
> ```
> restCall(Method.GET, "/api/internal/marketdata/test-water?testType", testWater _)
>     .withCircuitBreaker(CircuitBreaker.identifiedBy("shared-testing")),
> ```
> 
>  
> 
> goal svc: Lagom-removed with test endpoint calling either instrument / marketdata svc
> 
> * serialize error using ServiceErrorCompat
> 
> ```
>   def testWater(service: String, testType: String, handleSvcErr: Boolean): Future[Done] = {
>     service match {
>       case "marketdata" =>
>         marketDataService.testWater(testType).invoke().recover {
>           case e: MarketDataSvcException =>
>             if (handleSvcErr)
>               throw GoalSvcException("Something wrong with MarketData svc", GoalSvcErrorType.SOMETHING_WRONG)
>             else throw e
>         }
>       case "instrument" =>
>         instrumentService.testWater(testType).invoke().recover {
>           case e: InstrumentSvcException =>
>             if (handleSvcErr)
>               throw GoalSvcException("Something wrong with Instrument svc", GoalSvcErrorType.SOMETHING_WRONG)
>             else throw e
>         }
>       case _ => Future.successful(Done)
>     }
>   }
> ```
> 
>  
> 
> advisory svc: Lagom with test endpoint calling either instrument / marketdata svc
> 
> * serialize error using `LagomServiceExceptionSerializer`
> * also wrap 4xx to Lagom BadRequest to avoid error logging, but this is optional \(also not in scope of this PR\)
> 
> ```
>   override def testWater(service: String, testType: String, handleSvcErr: Boolean): ServiceCall[NotUsed, Done] = {
>     LagomExceptionWrappedServiceCall { _ =>
>       service match {
>         case "marketdata" =>
>           marketDataService.testWater(testType).invoke().recover {
>             case e: MarketDataSvcException =>
>               if (handleSvcErr)
>                 throw AdvisorySvcException("Something wrong with MarketData svc", AdvisorySvcErrorType.SOMETHING_WRONG)
>               else throw e
>           }
>         case "instrument" =>
>           instrumentService.testWater(testType).invoke().recover {
>             case e: InstrumentSvcException =>
>               if (handleSvcErr)
>                 throw AdvisorySvcException("Something wrong with Instrument svc", AdvisorySvcErrorType.SOMETHING_WRONG)
>               else throw e
>           }
>         case _ => Future.successful(Done)
>       }
>     }
> ```
> 
>  
> 
> instrument svc: Lagom-removed with test heavy endpoints
> 
> ```
>   def testHeavy: Future[Done] = {
>     Future { Thread.sleep(15000) }.map(_ => Done)
>   }
>   
>   Api.testHeavy impl { _ => testHeavy },
>   Api.testHeavyWithShortTimeout impl (_ => testHeavy, CustomTimeoutProcess(10.seconds)),
> ```
> 
> ## Test scenarios
> 
> Verified that error serdes works as expected \(as per `LagomServiceExceptionSerializerSpec` / `LagomCompatServiceExceptionSerializerSpec` / `ServiceErrorCompatSpec` \) for all combinations of:
> 
> * calling various testType in test endpoint of instrument/marketdata
> * calling various testType \+ option to handle underlying SvcException in test endpoint of advisory/goal \(forwarding to instrument/marketdata\)
> 
> Verified that if we use same `CircuitBreaker.identifiedBy("shared-testing")` in both instrument and marketdata endpoints, if one triggers circuit breaker, it will affect the other.
> 
> Verified that exception whitelist works as expected. No circuit breaker triggered for BadRequest/NotFound
> 
> Verified that endpoint specific request timeout works as expected. Able to return custom error json \(so that other services can deserialize\) instead of the default text response.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Full test matrix retained: Lagom/compat serializers, handled and forwarded service exceptions, shared breaker coupling, whitelist, endpoint timeout and custom JSON response. Source snippets are test setup, not production recommendations.
- Related source rows 2038, 2040, 2041: Keep uncertain getClass observation, reported compatibility test matrix and service-prefixed breaker correction distinct.

**Evidence:** anon-2.jsonl:2040 · comment 424733479 · PR 6845 · 2023-09-04

## A3-0219 — Cross-service heavyProcess breaker collision: prefix service name and keep default-superHeavyProcess

**Source stance:** explanation

**Context:**

> conf-reference/src/main/resources/lagom/lagom-circuit-breaker.conf; PR: [INV-1974] feat(all-services): Consolidate svc exception serdes + circuit breaker config

**Source-preserving request, proposal, or question:**

> So we used to have circuit breaker ids as `heavyProcess` / `superHeavyProcess`. Using same name across services will trigger each other’s circuit breaker.
> 
> I kept this name, but add svc name as prefix, e.g. `performance-superHeavyProcess`. And hence the default one is `default-superHeavyProcess`
> 
> I think it’s ok to keep it like this for now

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Related source rows 2038, 2040, 2041: Keep uncertain getClass observation, reported compatibility test matrix and service-prefixed breaker correction distinct.

**Evidence:** anon-2.jsonl:2041 · comment 425559128 · PR 6845 · 2023-09-07

Source path: `conf-reference/src/main/resources/lagom/lagom-circuit-breaker.conf`

**Evidence:** anon-2.jsonl:2041 · comment 425559128 · PR 6845 · 2023-09-07

Source path: `conf-reference/src/main/resources/lagom/lagom-circuit-breaker.conf`

**Explicit source context (hunk):**

> +    ]
> +  }
> +
> +  default-slowProcess {
> +    call-timeout = 20s
> +  }
> +  default-heavyProcess {

## A3-0241 — BasePlanRecurringInvestmentScheduleManager.scala: Retry for this too, in case we have any transient error

**Source stance:** requested-change

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/managers/BasePlanRecurringInvestmentScheduleManager.scala; PR: [EN-1992] Add support for recurring investment expiring communications

**Source-preserving request, proposal, or question:**

> Retry for this too, in case we have any transient error

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2064 · comment 425177909 · PR 6715 · 2023-09-06

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/managers/BasePlanRecurringInvestmentScheduleManager.scala`

**Evidence:** anon-2.jsonl:2064 · comment 425177909 · PR 6715 · 2023-09-06

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/managers/BasePlanRecurringInvestmentScheduleManager.scala`

**Explicit source context (hunk):**

> +        .zipWithIndex
> +        .wireTap { retrievedCustomerWithIndex =>
> +          {
> +            val (schedule, index) = retrievedCustomerWithIndex
> +            val count = index + 1
> +            logger.info(
> +              s"[RECURRING-EXPIRED-TRIGGER][count: $count] for plan ${schedule.planId} for customer ${schedule.customerId}|${schedule.tradingAccountType} using the date [$executeDate]"

## A3-0243 — PlanCommunicationV2EventProcessor.scala: Can we extract this communication sending to separate method so it’s easier to follow? ``` event.removalReason match { case Some(RecurringInvestmentSc

**Source stance:** suggestion

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala; PR: [EN-2017] Add support for recurring investment expired removal

**Source-preserving request, proposal, or question:**

> Nit: Can we extract this communication sending to separate method so it’s easier to follow?
> 
> ```
> event.removalReason match {
>   case Some(RecurringInvestmentScheduleRemovalReason.Expiration) | Some(RecurringInvestmentScheduleRemovalReason.Deactivation) =>
>     logger.info(
>       s"skipping to send email RECURRING_INVESTMENT_STOPPED for customer [${event.customerId}] due to [${event.removalReason}] removal reason!"
>     )
>     Future.successful(Done)
>   case Some(removalReason) =>
>     sendRecurringInvestmentStoppedCommunication(event, previousSchedule, removalReason)
>   case None =>
>     sendRecurringInvestmentStoppedCommunication(event, previousSchedule, RecurringInvestmentScheduleRemovalReason.IsOtherCancellation)
> }
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2066 · comment 424832352 · PR 6804 · 2023-09-05

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

> Nit: Can we extract this communication sending to separate method so it’s easier to follow?
> 
> ```
> event.removalReason match {
>   case Some(RecurringInvestmentScheduleRemovalReason.Expiration) | Some(RecurringInvestmentScheduleRemovalReason.Deactivation) =>
>     logger.info(
>       s"skipping to send email RECURRING_INVESTMENT_STOPPED for customer [${event.customerId}] due to [${event.removalReason}] removal reason!"
>     )
>     Future.successful(Done)
>   case Some(removalReason) =>
>     sendRecurringInvestmentStoppedCommunication(event, previousSchedule, removalReason)
>   case None =>
>     sendRecurringInvestmentStoppedCommunication(event, previousSchedule, RecurringInvestmentScheduleRemovalReason.IsOtherCancellation)
> }
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2066 · comment 424832352 · PR 6804 · 2023-09-05

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Explicit source context (hunk):**

> -        } yield Done
> +            Future.successful(Done)
> +          case Some(removalReason) =>
> +            sendRecurringInvestmentStoppedCommunication(event, previousSchedule, removalReason)
> +          case None =>
> +            sendRecurringInvestmentStoppedCommunication(event, previousSchedule, RecurringInvestmentScheduleRemovalReason.Others)
> +        }

## A3-0244 — Idempotent command permits bounded AskTimeout retry

**Source stance:** explanation

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/managers/BasePlanRecurringInvestmentScheduleManager.scala; PR: [EN-2017] Add support for recurring investment expired removal

**Source-preserving request, proposal, or question:**

> This cmd should be idempotent so it’s safe to retry a few times before giving up. Helps us avoid toil on transient issues like AskTimeout

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2067 · comment 424832834 · PR 6804 · 2023-09-05

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/managers/BasePlanRecurringInvestmentScheduleManager.scala`

**Evidence:** anon-2.jsonl:2067 · comment 424832834 · PR 6804 · 2023-09-05

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/managers/BasePlanRecurringInvestmentScheduleManager.scala`

**Explicit source context (hunk):**

> +    planId: UUID,
> +    schedule: RecurringTransactionSchedule
> +  ): Future[Done] = {
> +    FutureUtils
> +      .futureWithRetry(
> +        fut = for {
> +          _ <- refProvider

## A3-0245 — PlanCommunicationV2EventProcessor.scala: Why we need to `.map(_ => Done)` again?

**Source stance:** open-question

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala; PR: [EN-2017] Add support for recurring investment expired removal

**Source-preserving request, proposal, or question:**

> Why we need to `.map(_ => Done)` again?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2068 · comment 425178267 · PR 6804 · 2023-09-06

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Evidence:** anon-2.jsonl:2068 · comment 425178267 · PR 6804 · 2023-09-06

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Explicit source context (hunk):**

> -        } yield Done
> +            Future.successful(Done)
> +          case Some(removalReason) =>
> +            sendRecurringInvestmentStoppedCommunication(event, previousSchedule, removalReason)
> +          case None =>
> +            sendRecurringInvestmentStoppedCommunication(event, previousSchedule, RecurringInvestmentScheduleRemovalReason.Others)
> +        }

## A3-0255 — RecurringInvestmentScheduleJdbcEventProcessor.scala: You’ll need for-comprehend block

**Source stance:** requested-change

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleJdbcEventProcessor.scala; PR: [EN-2021] Add readside table for plan recurring investment

**Source-preserving request, proposal, or question:**

> You’ll need for-comprehend block

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2078 · comment 422182815 · PR 6740 · 2023-08-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleJdbcEventProcessor.scala`

**Evidence:** anon-2.jsonl:2078 · comment 422182815 · PR 6740 · 2023-08-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleJdbcEventProcessor.scala`

**Explicit source context (hunk):**

> +
> +  private[processors] def handlePlanCreated(ele: EventEnvelope[PlanCreatedEvt]): Future[Unit] = {
> +    val event = ele.event
> +    for {
> +      _ <- upsert(
> +        ele = ele,
> +        goalId = event.plan.goalId,

## A3-0265 — UpdatedEvt old/new inserts and offset-commit failures: duplicate windows and PK alternatives

**Source stance:** explanation

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleJdbcEventProcessor.scala; PR: [EN-2021] Add readside table for plan recurring investment

**Concern stated in the source:** Even with separate processors, the chance of duplicated rows is still there because we perform 2 inserts for UpdatedEvt \(but yes, splitting the processors reduce this chance much further\)

Even for event with single insert, duplicates can happen if insert succeeds and offset commit fails.

If data side is able to handle the \(rare\) duplicates, I’d say we stick with no pk.

However, if data side insists we cannot have duplicates, then as  suggested, generate a fake UUID based on the fields, and use it as pk.

Let’s not add a composite key so many fields, as under the hood, pg would create index for them too - which is useless because we are not querying this table at all from application side?

**Source-preserving request, proposal, or question:**

> Even with separate processors, the chance of duplicated rows is still there because we perform 2 inserts for UpdatedEvt \(but yes, splitting the processors reduce this chance much further\)
> 
> Within the history processor itself, this can still happen for UpdatedEvt if:
> 
> * insert old succeeds, but insert new fails → retry for the event, which will insert old again
> * insert old succeeds, insert new also succeeds, but offset commit fails → retry for the event, which will insert both again
> 
> Even for event with single insert, duplicates can happen if insert succeeds and offset commit fails.
> 
> 
> 
> If data side is able to handle the \(rare\) duplicates, I’d say we stick with no pk. I’m skeptical with the amount of fields in this composite key too.
> 
> However, if data side insists we cannot have duplicates, then as  suggested, generate a fake UUID based on the fields, and use it as pk. Let’s not add a composite key so many fields, as under the hood, pg would create index for them too - which is useless because we are not querying this table at all from application side?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Retain all insert/offset-commit windows, tolerated-duplicate branch versus deterministic fake UUID PK alternative, and objection to wide composite index.
- Related source rows 2080, 2086, 2089: History PK opinion evolves from broad composite suggestion to duplicate-tolerance or fakeUUID PK; do not flatten to mandatory wide composite key.

**Evidence:** anon-2.jsonl:2089 · comment 422620412 · PR 6740 · 2023-08-28

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleJdbcEventProcessor.scala`

> Even with separate processors, the chance of duplicated rows is still there because we perform 2 inserts for UpdatedEvt \(but yes, splitting the processors reduce this chance much further\)
> 
> Within the history processor itself, this can still happen for UpdatedEvt if:
> 
> * insert old succeeds, but insert new fails → retry for the event, which will insert old again
> * insert old succeeds, insert new also succeeds, but offset commit fails → retry for the event, which will insert both again
> 
> Even for event with single insert, duplicates can happen if insert succeeds and offset commit fails.
> 
> ‌
> 
> If data side is able to handle the \(rare\) duplicates, I’d say we stick with no pk. I’m skeptical with the amount of fields in this composite key too.
> 
> However, if data side insists we cannot have duplicates, then as

**Evidence:** anon-2.jsonl:2089 · comment 422620412 · PR 6740 · 2023-08-28

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleJdbcEventProcessor.scala`

> suggested, generate a fake UUID based on the fields, and use it as pk. Let’s not add a composite key so many fields, as under the hood, pg would create index for them too - which is useless because we are not querying this table at all from application side?
> 
> ‌

## A3-0304 — RecurringInvestmentFrequencyDetailUtilTest.scala: No future so you can just use AnyWordSpec

**Source stance:** requested-change

**Context:**

> goal-impl/src/test/scala/com/endowus/silver/goal/impl/helpers/RecurringInvestmentFrequencyDetailUtilTest.scala; PR: [EN-2023][EN-2007](invest) Upcoming recurring investment, recurring investment cancel email/platform notifications

**Source-preserving request, proposal, or question:**

> No future so you can just use AnyWordSpec

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2129 · comment 421223639 · PR 6724 · 2023-08-22

Source path: `goal-impl/src/test/scala/com/endowus/silver/goal/impl/helpers/RecurringInvestmentFrequencyDetailUtilTest.scala`

**Evidence:** anon-2.jsonl:2129 · comment 421223639 · PR 6724 · 2023-08-22

Source path: `goal-impl/src/test/scala/com/endowus/silver/goal/impl/helpers/RecurringInvestmentFrequencyDetailUtilTest.scala`

**Explicit source context (hunk):**

> +
> +import java.time.LocalDate
> +
> +class RecurringInvestmentFrequencyDetailUtilTest extends AsyncWordSpec with Matchers {
> +
> +  "constructUserFriendlyFrequencyDetail" should {
> +    "construct frequency detail for weekly interval without endDetails" in {

## A3-0310 — PlanCommunicationV2EventProcessor.scala: So we’re ok to fire and forget here?

**Source stance:** open-question

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala; PR: [EN-1990] Email/PlatformNotification for recurring setup, modify, stop

**Source-preserving request, proposal, or question:**

> So we’re ok to fire and forget here?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2135 · comment 420900763 · PR 6686 · 2023-08-21

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Evidence:** anon-2.jsonl:2135 · comment 420900763 · PR 6686 · 2023-08-21

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Explicit source context (hunk):**

> +
> +        val emailRequest = new EmailRequest(
> +          customerId = plan.customerId,
> +          communicationId = communicationId,
> +          requestedAt = instantNow,
> +          providerData = SendgridData(
> +            localeToTemplateId = Map(Locale.EN_HK -> "

**Evidence:** anon-2.jsonl:2135 · comment 420900763 · PR 6686 · 2023-08-21

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Explicit source context (hunk):**

> ", Locale.EN_SG -> "

**Evidence:** anon-2.jsonl:2135 · comment 420900763 · PR 6686 · 2023-08-21

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Explicit source context (hunk):**

> "),

## A3-0323 — Three-MCCY-broker creation: partial success, retry and stale active-account readside

**Source stance:** open-question

**Context:**

> broker-impl/src/main/scala/com/endowus/silver/broker/impl/logic/service/BaseBrokerServiceLogicImpl.scala; PR: [INV-1723]: feat(broker): SG - add create mccy brokers on base broker creation via event processor handler

**Concern stated in the source:** * event processor catches exception and retries
* the flow queries active broker accounts - which might still not return 1st in the list yet due to eventual consistency
* we might invoke `CreateBrokerAccountCmd` again for 1st?

**Source-preserving request, proposal, or question:**

> Thinking out loud… say we are creating 3 mccy brokers, 1st succeeded, 2nd failed due to whatever reason
> 
> * event processor catches exception and retries
> * the flow queries active broker accounts - which might still not return 1st in the list yet due to eventual consistency
> * we might invoke `CreateBrokerAccountCmd` again for 1st? And it seems the cmd handler is not idempotent?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Keep exact three-MCCY-broker partial-success/retry/eventual-readside/non-idempotent-create scenario as an unresolved concern.

**Evidence:** anon-2.jsonl:2148 · comment 419067251 · PR 6580 · 2023-08-14

Source path: `broker-impl/src/main/scala/com/endowus/silver/broker/impl/logic/service/BaseBrokerServiceLogicImpl.scala`

> Thinking out loud… say we are creating 3 mccy brokers, 1st succeeded, 2nd failed due to whatever reason
> 
> * event processor catches exception and retries
> * the flow queries active broker accounts - which might still not return 1st in the list yet due to eventual consistency
> * we might invoke `CreateBrokerAccountCmd` again for 1st? And it seems the cmd handler is not idempotent?
> 
> ‌

## A3-0377 — SgPlanUpsertConfirmationBehaviour.scala: This part looks a bit weird to me, cuz these 2 requests are now independent of each other. In theory we shouldn’t have to match them together. ``` for

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/planupsert/sg/SgPlanUpsertConfirmationBehaviour.scala; PR: [EN-1790] Update requests and dtos in advisory api

**Concern stated in the source:** This part looks a bit weird to me, cuz these 2 requests are now independent of each other.

**Source-preserving request, proposal, or question:**

> This part looks a bit weird to me, cuz these 2 requests are now independent of each other. In theory we shouldn’t have to match them together.
> 
> ```
> for {
>   maybeInvestmentResponse <- oneTimeInvestmentRequest.map {...}.getOrElse(Future of None)
>   updatedPlan <- recurringInvestmentRequest.map {...}.getOrElse(Future to fetch plan by id)
> } yield planUpsertConfirmationMapper(updatedPlan, maybeInvestmentResponse)
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2203 · comment 414432925 · PR 6524 · 2023-07-26

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/planupsert/sg/SgPlanUpsertConfirmationBehaviour.scala`

> This part looks a bit weird to me, cuz these 2 requests are now independent of each other. In theory we shouldn’t have to match them together.
> 
> ```
> for {
>   maybeInvestmentResponse <- oneTimeInvestmentRequest.map {...}.getOrElse(Future of None)
>   updatedPlan <- recurringInvestmentRequest.map {...}.getOrElse(Future to fetch plan by id)
> } yield planUpsertConfirmationMapper(updatedPlan, maybeInvestmentResponse)
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2203 · comment 414432925 · PR 6524 · 2023-07-26

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/planupsert/sg/SgPlanUpsertConfirmationBehaviour.scala`

**Explicit source context (hunk):**

> ).map {
> -          case (updatedPlan, investmentResponse) => planUpsertConfirmationMapper(updatedPlan, Some(investmentResponse))
> +          case (_, investmentResponse) => Some(investmentResponse)
>          }
> -      case MonthlyInvestmentRequest(amount, _) if amount == 0 =>
> -        stopPlanRecurringInvestment(goalId = goal.goalId, planId = existingPlanId).map(planUpsertConfirmationMapper(_, None))
> -      case MonthlyInvestmentRequest(amount, dayOfMonth) =>

## A3-0378 — SgInvestmentServiceImpl.scala: Better to just inject db directly into `investmentScheduleActivePeriodJdbcRepository` and the methods can return Future instead of DBIO

**Source stance:** suggestion

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/SgInvestmentServiceImpl.scala; PR: [ONB-2585] Add endpoint to retrieve missing recurring investments

**Source-preserving request, proposal, or question:**

> Better to just inject db directly into `investmentScheduleActivePeriodJdbcRepository` and the methods can return Future instead of DBIO

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2205 · comment 416502920 · PR 6619 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/SgInvestmentServiceImpl.scala`

**Evidence:** anon-2.jsonl:2205 · comment 416502920 · PR 6619 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/SgInvestmentServiceImpl.scala`

**Explicit source context (hunk):**

> val entityInspection: TypedEntityInspectionService,
>    val serviceLogic: ServiceLogic,
>    val localConfig: LocalConfig,
>    val system: ActorSystem,
> +  dateTimeProvider: DateTimeProvider,
> +  investmentScheduleActivePeriodJdbcRepository: InvestmentScheduleActivePeriodJdbcRepository
>  )(implicit val executionContext: ExecutionContext, val materializer: Materializer)

## A3-0401 — InvestmentScheduleActivePeriodJdbcEventProcessor.scala: the better syntax would be ``` _ <- investmentPlan.recurringInvestmentSchedule match { case Some(schedule) => repository.upsert(...) case None => Futu

**Source stance:** suggestion

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala; PR: [ONB-2557] Add readside for recurring investment schedules with their active periods

**Source-preserving request, proposal, or question:**

> Nit: the better syntax would be
> 
> ```
> _ <- investmentPlan.recurringInvestmentSchedule match {
>   case Some(schedule) => repository.upsert(...)
>   case None => Future.successful(Done)
> }
> ```
> 
> This way you don’t need to call Option.get

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2228 · comment 416513540 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Evidence:** anon-2.jsonl:2228 · comment 416513540 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Explicit source context (hunk):**

> +      _ <- investmentPlanFromEvt.recurringInvestmentSchedule match {
> +        case Some(_) =>
> +          investmentScheduleActivePeriodJdbcRepository.upsert(
> +            InvestmentScheduleActivePeriod(
> +              customerId = investmentPlanFromEvt.customerId,
> +              tradingAccountType = investmentPlanFromEvt.tradingAccountType,
> +              planId = planId,

## A3-0415 — SgServiceLogicImpl.scala: For timing, we can import `TimeUtils.TimedLogger` and simply call ``` logger.logTime(context) { fut } ```

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala; PR: Feat/INV-1633/goal perf across risk targets

**Source-preserving request, proposal, or question:**

> For timing, we can import `TimeUtils.TimedLogger` and simply call 
> 
> ```
> logger.logTime(context) { fut }
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2245 · comment 409391369 · PR 6389 · 2023-07-07

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala`

> For timing, we can import `TimeUtils.TimedLogger` and simply call 
> 
> ```
> logger.logTime(context) { fut }
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2245 · comment 409391369 · PR 6389 · 2023-07-07

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +            } yield riskTarget -> performanceMetrics
> +          }
> +          .runWith(Sink.seq)
> +          .map(_.toMap)
> +
> +        goalRiskTarget = ModelPortfolioRiskTarget.calculateRiskTargetFromStockRatio(goal.targetStockRatio)
> +        goalPerformanceMetrics = riskTargetPerformanceMetricsMap

## A3-0420 — Risk-target performance example uses mapAsync2 over risks and mapAsync1 over plans

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala; PR: Feat/INV-1633/goal perf across risk targets

**Source-preserving request, proposal, or question:**

> I give it a go…
> 
> ```
> riskTargetPerformanceMetricsMap <- Source(riskTargets)
>   .mapAsync(2) { riskTarget =>
>     val riskToleranceLevel = RiskToleranceUtils.riskToleranceLevelForUsage(riskTarget)
>     val targetStockRatio = RiskToleranceUtils.mapToTargetStockRatioForGeneralInvesting(riskToleranceLevel).getOrElse(...)
>     for {
>       planRiskTargetPortfolioTaaMap <- Source(validPlans)
>         .mapAsync(1) { plan =>
>           lookupProductPortfolioTaa(advisoryTag, targetStockRatio, plan.tradingAccountType).map(plan.planId -> _)
>         }
>         .runWith(Sink.seq)
>         .map(_.toMap)
> 
>       riskTargetGoalTaa = generateCombinedTaa(planMarketValues, planRiskTargetPortfolioTaaMap)
> 
>       performanceMetrics <- getPerformanceMetrics(taa = riskTargetGoalTaa, ccy = planCcy, period = PerformanceMetricsPeriodEnum.COMMON)
>         .map(response => response.performanceMetrics)
>     } yield riskTarget -> performanceMetrics
>   }
>   .runWith(Sink.seq)
>   .map(_.toMap)
> 
> goalRiskTarget = ModelPortfolioRiskTarget.calculateRiskTargetFromStockRatio(goal.targetStockRatio)
> goalPerformanceMetrics = riskTargetPerformanceMetricsMap.find(goalRiskTarget).getOrElse(...)
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Preserve nested mapAsync parallelism 2 over riskTargets and 1 over validPlans, risk ratio mapping, common-period performance, and goal risk lookup.

**Evidence:** anon-2.jsonl:2250 · comment 411332427 · PR 6389 · 2023-07-14

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala`

> I give it a go…
> 
> ```
> riskTargetPerformanceMetricsMap <- Source(riskTargets)
>   .mapAsync(2) { riskTarget =>
>     val riskToleranceLevel = RiskToleranceUtils.riskToleranceLevelForUsage(riskTarget)
>     val targetStockRatio = RiskToleranceUtils.mapToTargetStockRatioForGeneralInvesting(riskToleranceLevel).getOrElse(...)
>     for {
>       planRiskTargetPortfolioTaaMap <- Source(validPlans)
>         .mapAsync(1) { plan =>
>           lookupProductPortfolioTaa(advisoryTag, targetStockRatio, plan.tradingAccountType).map(plan.planId -> _)
>         }
>         .runWith(Sink.seq)
>         .map(_.toMap)
> 
>       riskTargetGoalTaa = generateCombinedTaa(planMarketValues, planRiskTargetPortfolioTaaMap)
> 
>       performanceMetrics <- getPerformanceMetrics(taa = riskTargetGoalTaa, ccy = planCcy, period = PerformanceMetricsPeriodEnum.COMMON)
>         .map(response => response.performanceMetrics)
>     } yield riskTarget -> performanceMetrics
>   }
>   .runWith(Sink.seq)
>   .map(_.toMap)
> 
> goalRiskTarget = ModelPortfolioRiskTarget.calculateRiskTargetFromStockRatio(goal.targetStockRatio)
> goalPerformanceMetrics = riskTargetPerformanceMetricsMap.find(goalRiskTarget).getOrElse(...)
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2250 · comment 411332427 · PR 6389 · 2023-07-14

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +          )
> +        advisoryTag = getAdvisoryTagFromProductLineAndIntent(product = productLineAndIntent)
> +        riskTargetPerformanceMetricsMap <- Source(riskTargets)
> +          .mapAsync(2) { riskTarget =>
> +            val riskToleranceLevel = RiskToleranceUtils.riskToleranceLevelForUsage(riskTarget)
> +            val targetStockRatio = RiskToleranceUtils.mapToTargetStockRatioForGeneralInvesting(riskToleranceLevel)
> +              .getOrElse(throw BadRequest(

## A3-0509 — FeeChargeRequestJdbcEventProcessorV5.scala: Hmm so we also update these planProfile too. I guess it’s fine cuz this will look up latest planProfile, but still feel very expensive :sweat_smile:

**Source stance:** explanation

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/jdbc/FeeChargeRequestJdbcEventProcessorV5.scala; PR: Resolve INV-1688: Add new projection table with tax details.

**Concern stated in the source:** I guess it’s fine cuz this will look up latest planProfile, but still feel very expensive :sweat_smile:

**Source-preserving request, proposal, or question:**

> Hmm so we also update these planProfile too. I guess it’s fine cuz this will look up latest planProfile, but still feel very expensive :sweat_smile:

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2345 · comment 408154820 · PR 6342 · 2023-07-03

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/jdbc/FeeChargeRequestJdbcEventProcessorV5.scala`

## A3-0514 — PlanTimeseriesTopicSubscriber.scala: ``` val DefaultFutureRetrySettings: FutureRetrySettings = FutureRetrySettings( minBackoff = 500.milliseconds, maxBackoff = 5.seconds, randomFactor = 0

**Source stance:** open-question

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/PlanTimeseriesTopicSubscriber.scala; PR: [INV-1303] feat(rebalance): Increase min backoff to 1.5s

**Source-preserving request, proposal, or question:**

> ```
> val DefaultFutureRetrySettings: FutureRetrySettings = FutureRetrySettings(
>   minBackoff = 500.milliseconds,
>   maxBackoff = 5.seconds,
>   randomFactor = 0.1,
>   maxRetries = 3,
> )
> ```
> 
> 
> 
> Are we sure just 1.5s min backoff is enough?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Current defaults min500ms/max5s/random0.1/maxRetries3; question asks whether1.5s minimum total is enough. Row2352 proposes5s/10s/3 instead.
- Related source rows 2350, 2352: Retry-default concern500ms/5s/3 is followed by5s/10s/3 proposal with readside-catch-up assumption.

**Evidence:** anon-2.jsonl:2350 · comment 406945479 · PR 6313 · 2023-06-28

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/PlanTimeseriesTopicSubscriber.scala`

> ```
> val DefaultFutureRetrySettings: FutureRetrySettings = FutureRetrySettings(
>   minBackoff = 500.milliseconds,
>   maxBackoff = 5.seconds,
>   randomFactor = 0.1,
>   maxRetries = 3,
> )
> ```
> 
> ‌
> 
> Are we sure just 1.5s min backoff is enough?
> 
> ‌

**Evidence:** anon-2.jsonl:2350 · comment 406945479 · PR 6313 · 2023-06-28

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/PlanTimeseriesTopicSubscriber.scala`

**Explicit source context (hunk):**

> },
> -              context = s"Trigger threshold breach check with retry for plan ID ${msg.planId}"
> +              context = s"Trigger threshold breach check with retry for plan ID ${msg.planId}",
> +              settings = DefaultFutureRetrySettings.copy(
> +                minBackoff = 5.seconds,
> +                maxBackoff = 10.seconds
> +              )

## A3-0516 — Readside TAA retry proposal5s-to10s/3 retries assumes no repeated TAA-updated event

**Source stance:** suggestion

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/PlanTimeseriesTopicSubscriber.scala; PR: [INV-1303] feat(rebalance): Increase min backoff to 1.5s

**Source-preserving request, proposal, or question:**

> So this retry will wait at least minBackoff and at most maxBackoff between each attempts, for upto maxRetries.
> 
> I think we can go with
> 
> ```
>   minBackoff = 5.seconds,
>   maxBackoff = 10.seconds,
>   maxRetries = 3,
> ```
> 
> so after 2nd attempt or at most 3rd attempt, readside TAA would catch up with state TAA \(assuming we don’t have repeated TAA updated evt\)

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Proposed retry min5s/max10s/maxRetries3 expects readside TAA catch-up by second/third attempt only assuming no repeated TAA-updated event.
- Related source rows 2350, 2352: Retry-default concern500ms/5s/3 is followed by5s/10s/3 proposal with readside-catch-up assumption.

**Evidence:** anon-2.jsonl:2352 · comment 407029610 · PR 6313 · 2023-06-28

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/PlanTimeseriesTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:2352 · comment 407029610 · PR 6313 · 2023-06-28

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/PlanTimeseriesTopicSubscriber.scala`

**Explicit source context (hunk):**

> },
> -              context = s"Trigger threshold breach check with retry for plan ID ${msg.planId}"
> +              context = s"Trigger threshold breach check with retry for plan ID ${msg.planId}",
> +              settings = DefaultFutureRetrySettings.copy(
> +                minBackoff = 5.seconds,
> +                maxBackoff = 10.seconds
> +              )

## A3-0527 — TaxExemptionManager.scala: Would returning Future\[Boolean\] match the `isCustomerExempted` better?

**Source stance:** open-question

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/TaxExemptionManager.scala; PR: Resolve INV-1709: Integrate tax exemption for charge

**Source-preserving request, proposal, or question:**

> Would returning Future\[Boolean\] match the `isCustomerExempted` better?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2364 · comment 406298702 · PR 6294 · 2023-06-26

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/TaxExemptionManager.scala`

**Evidence:** anon-2.jsonl:2364 · comment 406298702 · PR 6294 · 2023-06-26

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/TaxExemptionManager.scala`

**Explicit source context (hunk):**

> .map(_.toList)
>    }
>  
> +  // TODO: Might evolve to a list of intervals as well depending on requirement changes
> +  def isCustomerExempted(customerId: UUID, startDate: LocalDate, endDate: LocalDate): Future[Boolean] = {
> +    getTaxExemptionStatusForCustomer(customerId).map(_.maybeTaxExemption.exists(_.status == TaxExemptionStatus.Exempted))

## A3-0529 — Idempotent fee projection handlers with noop-catch-up then new-flow second release

**Source stance:** suggestion

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/sg/SgFeeManagerProjection.scala; PR: [INV-1709] feat(charge): SG charge logic for GST

**Concern stated in the source:** * 1st release, just rollout the projection with noop handlers so that the projection fully catch up with all events without applying any logic
* 2nd release, add everything else to start consuming in new flow

**Source-preserving request, proposal, or question:**

> These handler method should be idempotent. On actual release, we can split into 2:
> 
> * 1st release, just rollout the projection with noop handlers so that the projection fully catch up with all events without applying any logic
> * 2nd release, add everything else to start consuming in new flow

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Preserve idempotent-handler requirement and optional two-release noop-catch-up then new-flow handlers.

**Evidence:** anon-2.jsonl:2367 · comment 405842985 · PR 6283 · 2023-06-23

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/sg/SgFeeManagerProjection.scala`

> These handler method should be idempotent. On actual release, we can split into 2:
> 
> * 1st release, just rollout the projection with noop handlers so that the projection fully catch up with all events without applying any logic
> * 2nd release, add everything else to start consuming in new flow
> 
> ‌

**Evidence:** anon-2.jsonl:2367 · comment 405842985 · PR 6283 · 2023-06-23

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/sg/SgFeeManagerProjection.scala`

**Explicit source context (hunk):**

> +
> +  private val migrator = new CassandraMigrator(session)
> +
> +  def start(): CassandraProjectionManager[FeeManagerEvt] = {
> +    ProjectionBuilder
> +      .cassandra[FeeManagerEvt]
> +      .setEventHandler[FeeChargeDiscountAppliedEvt](ele => handleFeeChargeDiscountAppliedEvt(ele))

## A3-0534 — InvestmentTransferEventProcessor.scala: We need to return Future to chain it here. Otherwise, event processor won’t wait for investOnce and `NotifyInvestmentProcessInitiatedCmd` to complete 

**Source stance:** requested-change

**Context:**

> trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/investmentTransfer/processors/InvestmentTransferEventProcessor.scala; PR: TT-2498 Update InvestmentTransferProjection to skip RedemptionCompletedEvt if target plan is deactivated

**Concern stated in the source:** Otherwise, event processor won’t wait for investOnce and `NotifyInvestmentProcessInitiatedCmd` to complete before moving to next evt

**Source-preserving request, proposal, or question:**

> We need to return Future to chain it here. Otherwise, event processor won’t wait for investOnce and `NotifyInvestmentProcessInitiatedCmd` to complete before moving to next evt

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2374 · comment 406027382 · PR 6290 · 2023-06-23

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/investmentTransfer/processors/InvestmentTransferEventProcessor.scala`

**Evidence:** anon-2.jsonl:2374 · comment 406027382 · PR 6290 · 2023-06-23

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/investmentTransfer/processors/InvestmentTransferEventProcessor.scala`

**Explicit source context (hunk):**

> +      .invoke()
> +      .map(p => p.deactivatedAt.nonEmpty)
> +      .flatMap {
> +
> +        case true =>
> +          // 2023-06-23: For transfers between plans (whereby we do a redemption followed by investment), if
> +          // the target plan was deactivated before the investment request was created, log this error for manual

## A3-0543 — common.conf: This will increase timeout for all endpoints. should we make request timeout configurable in `EndpointExtensions#impl` using `Directives#withRequestTi

**Source stance:** open-question

**Context:**

> portfolio-impl/src/main/resources/common.conf; PR: Fix/EN-1685 increase request timeout for portfolio

**Source-preserving request, proposal, or question:**

> This will increase timeout for all endpoints.
> 
>   should we make request timeout configurable in `EndpointExtensions#impl` using `Directives#withRequestTimeout`

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2385 · comment 403954675 · PR 6231 · 2023-06-16

Source path: `portfolio-impl/src/main/resources/common.conf`

> This will increase timeout for all endpoints.

**Evidence:** anon-2.jsonl:2385 · comment 403954675 · PR 6231 · 2023-06-16

Source path: `portfolio-impl/src/main/resources/common.conf`

> should we make request timeout configurable in `EndpointExtensions#impl` using `Directives#withRequestTimeout`

**Evidence:** anon-2.jsonl:2385 · comment 403954675 · PR 6231 · 2023-06-16

Source path: `portfolio-impl/src/main/resources/common.conf`

**Explicit source context (hunk):**

> http {
>      routing.decode-max-size = 10000k
> +    server.request-timeout = 60s
>    }
>  }

## A3-0557 — PortfolioSuitabilityAnalysisLogic.scala: How about we create a local scaffiene cache for instrument performance in this method \(i.e. invalidate all after we are done with all the `instrument

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/PortfolioSuitabilityAnalysisLogic.scala; PR: Feat/INV-1551 be advisory modify fundsmart

**Source-preserving request, proposal, or question:**

> How about we create a local scaffiene cache for instrument performance in this method \(i.e. invalidate all after we are done with all the `instrumentWeights`\)
> 
> The lookup count is same, but maybe code is cleaner?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2402 · comment 402475537 · PR 6165 · 2023-06-12

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/PortfolioSuitabilityAnalysisLogic.scala`

## A3-0571 — Only transient errors should throw in EventProcessor/TopicSubscriber to avoid stuck data errors

**Source stance:** requested-change

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/EmailDataFactory.scala; PR: [INV-1354] feat(email):SG only, investment completed - update sendgrid payload to include investment request order details

**Concern stated in the source:** If data is wrong, this will cause the EventProcessor/TopicSubscriber to get stuck

**Source-preserving request, proposal, or question:**

> We should only throw if transient error that would go away after retry. If data is wrong, this will cause the EventProcessor/TopicSubscriber to get stuck

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2418 · comment 398531097 · PR 5978 · 2023-05-29

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/EmailDataFactory.scala`

**Evidence:** anon-2.jsonl:2418 · comment 398531097 · PR 5978 · 2023-05-29

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/EmailDataFactory.scala`

**Explicit source context (hunk):**

> +          confirmedPrice = order.confirmedPrice.map(price => FormatterUtils.FourDecimalPointNumberFormatter.format(price)),
> +          buySell = BuySell.BUY // Assumption that investment orders are always buy
> +        )
> +      }
> +    )
> +    view
> +  }

## A3-0573 — BrokerAccountTopicSubscriberCommunicationLogic.scala: Since it’s within investment svc, should we inject refProvider and just use ``` investmentRequests <- refProvider.getPlanInvestmentManagerEntityRef(UU

**Source stance:** suggestion

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/subscribers/BrokerAccountTopicSubscriberCommunicationLogic.scala; PR: [EN-982] fix(investment): ignore if there is no pending investment

**Source-preserving request, proposal, or question:**

> Since it’s within investment svc, should we inject refProvider and just use
> 
> ```
> investmentRequests <- refProvider.getPlanInvestmentManagerEntityRef(UUID.fromString(planId)).ask(GetPendingInitialInvestmentRequestCmd(_))
> ```
> 
> 
> 
> So we don’t have wonky exception handling here

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2420 · comment 401774605 · PR 6162 · 2023-06-08

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/subscribers/BrokerAccountTopicSubscriberCommunicationLogic.scala`

> Since it’s within investment svc, should we inject refProvider and just use
> 
> ```
> investmentRequests <- refProvider.getPlanInvestmentManagerEntityRef(UUID.fromString(planId)).ask(GetPendingInitialInvestmentRequestCmd(_))
> ```
> 
> ‌
> 
> So we don’t have wonky exception handling here

**Evidence:** anon-2.jsonl:2420 · comment 401774605 · PR 6162 · 2023-06-08

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/subscribers/BrokerAccountTopicSubscriberCommunicationLogic.scala`

**Explicit source context (hunk):**

> +                            )
> +                          ),
> +                          category = Category.PLATFORM
>                          )
> -                      ),
> -                      category = Category.PLATFORM
> +                      )

## A3-0594 — BrokerCommunicationV2EventProcessor.scala: Just curious, why change to def here? Wouldn’t it be simpler to val it \(let it start running\), and we simply wait for it in the for yield block \(me

**Source stance:** open-question

**Context:**

> broker-impl/src/main/scala/com/endowus/silver/broker/impl/entities/account/processors/BrokerCommunicationV2EventProcessor.scala; PR: Feat/EN-982 migrate one time platform notification

**Concern stated in the source:** Wouldn’t it be simpler to val it \(let it start running\), and we simply wait for it in the for yield block \(means we also need to use Future.sequence\)

**Source-preserving request, proposal, or question:**

> Just curious, why change to def here? Wouldn’t it be simpler to val it \(let it start running\), and we simply wait for it in the for yield block \(means we also need to use Future.sequence\)

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2441 · comment 398868114 · PR 5862 · 2023-05-30

Source path: `broker-impl/src/main/scala/com/endowus/silver/broker/impl/entities/account/processors/BrokerCommunicationV2EventProcessor.scala`

**Evidence:** anon-2.jsonl:2441 · comment 398868114 · PR 5862 · 2023-05-30

Source path: `broker-impl/src/main/scala/com/endowus/silver/broker/impl/entities/account/processors/BrokerCommunicationV2EventProcessor.scala`

**Explicit source context (hunk):**

> -    val maybeEmail1: Future[Unit] = maybeSendSgReadyToInvestEmail(
> +    val readyToInvestEmail: Future[Unit] = maybeSendSgReadyToInvestEmail(
>        regionalCustomer = regionalCustomer,
>        broker = broker,
>        brokerAccountNumber = brokerAccountNumber,
>        accountCcy = accountCcy,
>        tradingAccountType = tradingAccountType,

## A3-0598 — BrokerAccountTopicSubscriberHandlers.scala: If we rethrow here, and it’s not transient error… the subscriber will get stuck

**Source stance:** observed-defect

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/subscribers/BrokerAccountTopicSubscriberHandlers.scala; PR: Feat/EN-982 migrate one time platform notification

**Concern stated in the source:** If we rethrow here, and it’s not transient error… the subscriber will get stuck

**Source-preserving request, proposal, or question:**

> If we rethrow here, and it’s not transient error… the subscriber will get stuck

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:2445 · comment 398911839 · PR 5862 · 2023-05-30

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/subscribers/BrokerAccountTopicSubscriberHandlers.scala`

## A3-0604 — Alts cash-reservation remote call in projection; Kafka request/result ideal lacks trading events

**Source stance:** explanation

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/FeeChargeRequestProjection.scala; PR: [INV-1300] feat(charge)(trading)(redemption): Cash reservation for Alts fee charge

**Source-preserving request, proposal, or question:**

> It’s fine to have remote call in projection class \(not fine in cmd handler\)
> 
> In ideal workflow situation:
> 
> * charge to publish kafka msg `FeeCashReservationRequestedMsg`
> * trading listens to charge topic, handles that msg and reserve cash
> * trading to publish kafka msg about the cash reservation results
> 
>     * today it doesn’t publish any messages for cash reservation at all
>     * there is no event for cash reservation failure
>     
> * charge to consume these cash reservation messages, and continue to flow
> 
> 
> 
> For the scope of this ticket, I went with the approach in this PR

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Remote call in projection tolerated for scope; ideal request/result Kafka workflow cannot fully exist today because trading publishes neither reservation messages nor failure event.

**Evidence:** anon-2.jsonl:2452 · comment 397445492 · PR 6057 · 2023-05-25

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/FeeChargeRequestProjection.scala`

> It’s fine to have remote call in projection class \(not fine in cmd handler\)
> 
> In ideal workflow situation:
> 
> * charge to publish kafka msg `FeeCashReservationRequestedMsg`
> * trading listens to charge topic, handles that msg and reserve cash
> * trading to publish kafka msg about the cash reservation results
> 
>     * today it doesn’t publish any messages for cash reservation at all
>     * there is no event for cash reservation failure
>     
> * charge to consume these cash reservation messages, and continue to flow
> 
> ‌
> 
> For the scope of this ticket, I went with the approach in this PR

## A3-0615 — Slick cleanUp proposal preserves streaming and avoids running result twice

**Source stance:** open-question

**Context:**

> akka-abstraction-layer/src/main/scala/com/endowus/silver/projection/SlickProjectionManager.scala; PR: TT-2311 Fix SlickProjectionManager#process to not execute transactions twice

**Source-preserving request, proposal, or question:**

> asTry scaladoc says
> 
> ```
> If possible, use andFinally or cleanUp instead, because those combinators, unlike asTry, support streaming.
> ```
> 
> 
> 
> would the below serve the same purpose? basically we just don’t want to trigger `result` again
> 
> ```
>       withMetrics(envelope, shardNo) { errorCounter =>
>         result.cleanUp(_.fold(DBIO.successful()) { _ =>
>           errorCounter()
>           DBIO.successful()
>         })
>       }
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Slick asTry scaladoc specifically recommends andFinally/cleanUp for streaming; cleanUp proposal must not trigger result twice.

**Evidence:** anon-2.jsonl:2464 · comment 396743883 · PR 6045 · 2023-05-23

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/projection/SlickProjectionManager.scala`

> asTry scaladoc says
> 
> ```
> If possible, use andFinally or cleanUp instead, because those combinators, unlike asTry, support streaming.
> ```
> 
> ‌
> 
> would the below serve the same purpose? basically we just don’t want to trigger `result` again
> 
> ```
>       withMetrics(envelope, shardNo) { errorCounter =>
>         result.cleanUp(_.fold(DBIO.successful()) { _ =>
>           errorCounter()
>           DBIO.successful()
>         })
>       }
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2464 · comment 396743883 · PR 6045 · 2023-05-23

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/projection/SlickProjectionManager.scala`

**Explicit source context (hunk):**

> +      })
> +
> +      withMetrics(envelope, shardNo) { errorCounterFunc =>
> +        dbio.asTry.flatMap {
> +          case Failure(_) =>
> +            errorCounterFunc()
> +            DBIO.successful(Done)

## A3-0616 — PortfolioService.scala: This endpoint is used by Davinci? Does this actually help at all, cuz circuit breaker config should be on client side?

**Source stance:** open-question

**Context:**

> portfolio-api/src/main/scala/com/endowus/silver/portfolio/api/PortfolioService.scala; PR: [EN-1546] Increase timeout for aaa endpoint

**Concern stated in the source:** Does this actually help at all, cuz circuit breaker config should be on client side?

**Source-preserving request, proposal, or question:**

> This endpoint is used by Davinci? Does this actually help at all, cuz circuit breaker config should be on client side?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2465 · comment 396715947 · PR 6044 · 2023-05-23

Source path: `portfolio-api/src/main/scala/com/endowus/silver/portfolio/api/PortfolioService.scala`

**Evidence:** anon-2.jsonl:2465 · comment 396715947 · PR 6044 · 2023-05-23

Source path: `portfolio-api/src/main/scala/com/endowus/silver/portfolio/api/PortfolioService.scala`

**Explicit source context (hunk):**

> "/api/v1/portfolio/edge/underlying-aaa?customerId&goalId&tradingAccountType",
>            getPortfolioUnderlyingAaa _
> -        ).withCircuitBreaker(CircuitBreaker.identifiedBy("heavyProcess")),
> +        ).withCircuitBreaker(CircuitBreaker.identifiedBy("superHeavyProcess")),
>          restCall(
>            Method.GET,
>            "/api/v1/portfolio/edge/underlying-taa?portfolioId&effectiveDate",

## A3-0687 — TransactionFxConverter.scala: Not good hide var like this \(e.g `maybeConvertedSettlementDetail` was a fut, and then reassigned as an Option How about just ``` maybeConvertedSettle

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/utils/TransactionFxConverter.scala; PR: [INV-1437] feat(transaction): Models

**Source-preserving request, proposal, or question:**

> Not good hide var like this \(e.g `maybeConvertedSettlementDetail` was a fut, and then reassigned as an Option
> 
> How about just
> 
> ```
> maybeConvertedSettlementDetail <- transaction.assetTransferDetails.flatMap(_.settledAssetTransferDetail) match {
>   case Some(value) => convertSettlementDetail(value).map(Some(_))
>   case None => Future.successful(None)
> }
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2538 · comment 391031530 · PR 5770 · 2023-05-02

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/utils/TransactionFxConverter.scala`

> Not good hide var like this \(e.g `maybeConvertedSettlementDetail` was a fut, and then reassigned as an Option
> 
> How about just
> 
> ```
> maybeConvertedSettlementDetail <- transaction.assetTransferDetails.flatMap(_.settledAssetTransferDetail) match {
>   case Some(value) => convertSettlementDetail(value).map(Some(_))
>   case None => Future.successful(None)
> }
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2538 · comment 391031530 · PR 5770 · 2023-05-02

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/utils/TransactionFxConverter.scala`

**Explicit source context (hunk):**

> +        ccy = targetCcy,
> +        amount = maybeConvertedSettlementDetail.flatMap(_.displayTransferDateAmount),
> +        originalAmount = maybeConvertedSettlementDetail.map(_.transferDateAmount),
> +        assetTransferDetails = transaction.assetTransferDetails.map(
> +          assetTransferDetails => assetTransferDetails.copy(
> +            settledAssetTransferDetail = maybeConvertedSettlementDetail
> +          )

## A3-0699 — UtilityManager.scala: log error and move on to next portfolioId instead of throwing and block the whole set

**Source stance:** requested-change

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/UtilityManager.scala; PR: Feat/INV-1447/sync with latest performance

**Source-preserving request, proposal, or question:**

> Let’s log error and move on to next portfolioId instead of throwing and block the whole set

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2550 · comment 387899786 · PR 5777 · 2023-04-19

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/UtilityManager.scala`

**Evidence:** anon-2.jsonl:2550 · comment 387899786 · PR 5777 · 2023-04-19

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/UtilityManager.scala`

**Explicit source context (hunk):**

> +              ccy = ccy,
> +              annualisedReturn = performance.annualisedReturn,
> +              annualisedVol = performance.annualisedVol,
> +              cumulativeReturn = performance.cumulativeReturn,
> +              monthlyReturnsMean = performance.monthlyReturnsAvg,
> +              monthlyReturnsVol = performance.monthlyReturnsVol,
> +              monthlyReturnStart = Some(performance.monthlyReturnStart),

## A3-0709 — SubscriberMetricsWithKamon.scala: recoverWith should return Future Use recover \+ throw or recoverWith \+ Future.failed

**Source stance:** requested-change

**Context:**

> silver-commons/src/main/scala/com/endowus/silver/commons/kafka/SubscriberMetricsWithKamon.scala; PR: Feat/INV-1151 rebalance entity refactor phase 2 projections

**Source-preserving request, proposal, or question:**

> recoverWith should return Future
> 
> Use recover \+ throw or recoverWith \+ Future.failed

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2561 · comment 382282896 · PR 5603 · 2023-03-29

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/kafka/SubscriberMetricsWithKamon.scala`

**Evidence:** anon-2.jsonl:2561 · comment 382282896 · PR 5603 · 2023-03-29

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/kafka/SubscriberMetricsWithKamon.scala`

**Explicit source context (hunk):**

> +        .recoverWith {
> +          case ex =>
> +            metrics.failureCounter.increment()
> +            Future.failed(ex)
> +        }
>        _ = timer.stop()
>      } yield Done

## A3-0711 — RebalancePlanJdbcRepository.scala: Seems identical to existing method? We can just change the old one to return Future?

**Source stance:** open-question

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/db/jdbc/RebalancePlanJdbcRepository.scala; PR: Feat/INV-1151 rebalance entity refactor phase 2 projections

**Source-preserving request, proposal, or question:**

> Seems identical to existing method? We can just change the old one to return Future?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2563 · comment 382284388 · PR 5603 · 2023-03-29

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/db/jdbc/RebalancePlanJdbcRepository.scala`

## A3-0747 — PlanTimeseriesTopicSubscriber.scala: TimedLogger#logTime already logs info when the future completes. Do we still need this log?

**Source stance:** open-question

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/PlanTimeseriesTopicSubscriber.scala; PR: [INV-1151] feat(rebalance): Added logging and up the timeout to 30s

**Source-preserving request, proposal, or question:**

> TimedLogger#logTime already logs info when the future completes. Do we still need this log?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2599 · comment 379644199 · PR 5524 · 2023-03-20

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/PlanTimeseriesTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:2599 · comment 379644199 · PR 5524 · 2023-03-20

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/PlanTimeseriesTopicSubscriber.scala`

**Explicit source context (hunk):**

> +      ) {
>          for {
> -          rebalancePlan <- refProvider.getPlanRebalancerEntityRef(msg.planId).ask(GetRebalancePlanCmd(_))
> +          rebalancePlan <- logger.logTime(s"Loading rebalance plan entity for planId ${msg.planId}") {
> +            refProvider.getPlanRebalancerEntityRef(msg.planId).ask(GetRebalancePlanCmd(_))
> +          }
>            _ <- if (rebalancePlan.isEmpty) {

## A3-0758 — Transaction FX conversion Futures: bounded Source.mapAsync2 proposed

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/utils/TransactionFxConverter.scala; PR: Feat/INV-913 tech debt fx rates

**Source-preserving request, proposal, or question:**

> I’m a little skeptical with spawning all the futures at once here. We would be capped by the number of cores anyway. Maybe the usual Source\(transactions\).mapAsync\(2\) \{….\} ?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2610 · comment 370756717 · PR 5266 · 2023-02-17

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/utils/TransactionFxConverter.scala`

**Evidence:** anon-2.jsonl:2610 · comment 370756717 · PR 5266 · 2023-02-17

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/utils/TransactionFxConverter.scala`

**Explicit source context (hunk):**

> +        .runWith(Sink.seq)
> +        .map(_.toList)
>      }
>    }
>  
> -  private def fetchFxRatesAndRefreshCache(baseCcy: CurrencyUnit, quoteCcy: CurrencyUnit): Future[List[(LocalDate, BigDecimal)]] = {
> -    logger.info(s"fetchFxRatesAndRefreshCache started for [$baseCcy$quoteCcy]...")

## A3-0759 — TransactionFxConverter.scala: Can we rename \+ declare type for this to indicate it’s a Option\[Future\]… otherwise I feel it’s a little confusing to read this block…

**Source stance:** requested-change

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/utils/TransactionFxConverter.scala; PR: Feat/INV-913 tech debt fx rates

**Concern stated in the source:** Can we rename \+ declare type for this to indicate it’s a Option\[Future\]… otherwise I feel it’s a little confusing to read this block…

**Source-preserving request, proposal, or question:**

> Can we rename \+ declare type for this to indicate it’s a Option\[Future\]… otherwise I feel it’s a little confusing to read this block…

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2611 · comment 370761680 · PR 5266 · 2023-02-17

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/utils/TransactionFxConverter.scala`

**Evidence:** anon-2.jsonl:2611 · comment 370761680 · PR 5266 · 2023-02-17

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/utils/TransactionFxConverter.scala`

**Explicit source context (hunk):**

> -            })
> +      res = transaction.copy(
> +        fxConversionDetails = transaction.fxConversionDetails.map(
> +          fxConversionDetails => fxConversionDetails.copy(
> +            settlementDetails = maybeConvertedSettlementDetail
> +          )
>          )

## A3-0774 — FxRateHelper.scala: ``` fxRateCache .getIfPresent(fxId) .map(Future.successful) .getOrElse(loadCacheAndFind(fxId)) ``` Try to use Option more idiomatically

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala; PR: Feat/INV-913 tech debt fx rates

**Source-preserving request, proposal, or question:**

> ```
> fxRateCache
>   .getIfPresent(fxId)
>   .map(Future.successful)
>   .getOrElse(loadCacheAndFind(fxId))
> ```
> 
> Try to use Option more idiomatically

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2628 · comment 377730484 · PR 5266 · 2023-03-14

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala`

**Evidence:** anon-2.jsonl:2628 · comment 377730484 · PR 5266 · 2023-03-14

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala`

**Explicit source context (hunk):**

> +          NO_FX_RATES_AVAILABLE
> +        )))
> +    }
> +  }
> +
> +  private def loadFxRates(baseCcy: CurrencyUnit, quoteCcy: CurrencyUnit) = {
> +    logger.logTime(s"Loading fx rates for baseCcy [$baseCcy] to quoteCcy [$quoteCcy] from source") {

## A3-0786 — ReportApplication.scala: The channels are supposed to be pooled… not sure why are we wiring it here…

**Source stance:** open-question

**Context:**

> report-impl/src/main/scala/com/endowus/silver/report/impl/ReportApplication.scala; PR: Feat/EN-870 sg auto generate report meta data

**Source-preserving request, proposal, or question:**

> The channels are supposed to be pooled… not sure why are we wiring it here…

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:2641 · comment 377383842 · PR 5350 · 2023-03-13

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/ReportApplication.scala`

## A3-0792 — SftpTask pooled channel runner versus long-held connection historical failures

**Source stance:** explanation

**Context:**

> report-impl/src/main/scala/com/endowus/silver/report/impl/statement/sftp/SftpMetadataChecker.scala; PR: Feat/EN-870 sg auto generate report meta data

**Concern stated in the source:** Here we are moving to back to the old process in which we take a channel, and apply long running logic with it - which caused a few issues in the past since the connection cannot last for too long

**Source-preserving request, proposal, or question:**

> The channels are pooled and any interactions with it are done via `SftpTask`. The runner takes care of invalidating/returning the channel if any errors occur.
> 
> Here we are moving to back to the old process in which we take a channel, and apply long running logic with it - which caused a few issues in the past since the connection cannot last for too long

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Pooled SftpTask runner must invalidate/return channels; long-running logic holding one connection recapitulates historical failures.

**Evidence:** anon-2.jsonl:2647 · comment 377385297 · PR 5350 · 2023-03-13

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/sftp/SftpMetadataChecker.scala`

**Evidence:** anon-2.jsonl:2647 · comment 377385297 · PR 5350 · 2023-03-13

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/sftp/SftpMetadataChecker.scala`

**Explicit source context (hunk):**

> +  def checkMetaDataAgainstPdfFiles(yearMonth: YearMonth): Future[Done] = {
> +    val directoryPath = sftpStatementGenerator.getTargetMonthDirectory(yearMonth)
> +
> +    val directoryExists = sftpRunner.execute(CheckDirectoryExistenceTask(directoryPath))
> +    if (!directoryExists) {
> +      val msg = s"Folder [$directoryPath] does not exist. Nothing to count"
> +      slackNotificationSender.sendSlackMessage(msg, SlackNotificationColorEnum.WARNING)

## A3-0799 — SftpTask.scala: Can we add a function to extract only data that we need? Returning the whole buffered reader is not good I think. Ofc being able to stream the output 

**Source stance:** suggestion

**Context:**

> silver-commons/src/main/scala/com/endowus/silver/commons/sftp/SftpTask.scala; PR: Feat/EN-870 sg auto generate report meta data

**Source-preserving request, proposal, or question:**

> Can we add a function to extract only data that we need? Returning the whole buffered reader is not good I think.
> 
> Ofc being able to stream the output is much better, but that doesn’t fit well into how this SftpTask works at the moment

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2654 · comment 379041565 · PR 5350 · 2023-03-17

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/sftp/SftpTask.scala`

**Evidence:** anon-2.jsonl:2654 · comment 379041565 · PR 5350 · 2023-03-17

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/sftp/SftpTask.scala`

**Explicit source context (hunk):**

> +  import scala.jdk.CollectionConverters._
> +  override def run(channelSftp: ChannelSftp): List[String] = {
> +    channelSftp.ls(directoryPath).asInstanceOf[util.Vector[ChannelSftp#LsEntry]].asScala.toList.map(_.getFilename)
> +  }
> +}
> +
> +case class ReadFileTask(directoryPath: String, fileName: String) extends SftpTask[immutable.Seq[String]] with StrictLogging {

## A3-0801 — SftpMetadataChecker.scala: This returns a try. So even if the below exception is thrown, the flow doesn’t stop

**Source stance:** observed-defect

**Context:**

> report-impl/src/main/scala/com/endowus/silver/report/impl/statement/sftp/SftpMetadataChecker.scala; PR: Feat/EN-870 sg auto generate report meta data

**Source-preserving request, proposal, or question:**

> This returns a try. So even if the below exception is thrown, the flow doesn’t stop

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2656 · comment 379042274 · PR 5350 · 2023-03-17

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/sftp/SftpMetadataChecker.scala`

**Evidence:** anon-2.jsonl:2656 · comment 379042274 · PR 5350 · 2023-03-17

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/sftp/SftpMetadataChecker.scala`

**Explicit source context (hunk):**

> +    val directoryExists = sftpRunner.execute(CheckDirectoryExistenceTask(directoryPath))
> +    if (!directoryExists) {
> +      val msg = s"Folder [$directoryPath] does not exist. Nothing to count"
> +      slackNotificationSender.sendSlackMessage(msg, SlackNotificationColorEnum.WARNING)
> +      throw ReportSvcException(msg, ReportSvcErrorType.SFTP_ERROR)
> +    }
> +

## A3-0804 — SftpMetadataChecker.scala: Do we need to throttle and `parallelism` = 1? I think it’s ok to just query with `parallelism` = 2 without throttling here

**Source stance:** open-question

**Context:**

> report-impl/src/main/scala/com/endowus/silver/report/impl/statement/sftp/SftpMetadataChecker.scala; PR: Feat/EN-870 sg auto generate report meta data

**Source-preserving request, proposal, or question:**

> Do we need to throttle and `parallelism` = 1? I think it’s ok to just query with `parallelism` = 2 without throttling here

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2659 · comment 379043482 · PR 5350 · 2023-03-17

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/sftp/SftpMetadataChecker.scala`

**Evidence:** anon-2.jsonl:2659 · comment 379043482 · PR 5350 · 2023-03-17

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/sftp/SftpMetadataChecker.scala`

**Explicit source context (hunk):**

> +        } yield info
> +      }
> +      .runWith(Sink.seq)
> +  }
> +
> +  private[sftp] def generateMessageCompareFileNamesInMetadataAndFilesInFolder(
> +    documentIdsInCsvFile: Seq[String],

## A3-0811 — AdvisedPortfolioOfferingsManager.scala: You can write this as ``` .mapAsyncUnordered(parallelism = 2) { case (portfolioId, effectiveDate) => ```

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/AdvisedPortfolioOfferingsManager.scala; PR: [INV-1116] feat(advisory, invest.20): Recommended core portfolios

**Source-preserving request, proposal, or question:**

> You can write this as
> 
> ```
> .mapAsyncUnordered(parallelism = 2) { case (portfolioId, effectiveDate) =>
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2666 · comment 373500037 · PR 5295 · 2023-02-28

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/AdvisedPortfolioOfferingsManager.scala`

> You can write this as
> 
> ```
> .mapAsyncUnordered(parallelism = 2) { case (portfolioId, effectiveDate) =>
> ```
> 
> ‌

## A3-0821 — Independent dividend files: BadRequest nonretry and bounded TCP/unknown retry

**Source stance:** explanation

**Context:**

> dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/subscribers/HongKongEntitlementDividendTopicSubscriber.scala; PR: TT-1732 change dividendTopic to dividendFileTopic

**Concern stated in the source:** Since we can’t reliably reproduce and fix them, we want to limit the number of retries to avoid blocking the whole topic.

**Source-preserving request, proposal, or question:**

> The ServiceLogic in dividend svc alreadymaps the scenarios it cannot handle the file to BadRequest. So we don’t want to waste time retrying for those case \(’s intention\).
> 
> There could potentially still be other exceptions that not caught by ServiceLogic itself, e.g. the case of big file and the tcp connection got cut during file processing. Since we can’t reliably reproduce and fix them, we want to limit the number of retries to avoid blocking the whole topic. Each dividend file should be independent, so we don’t care about their ordering \(unlike events in other normal topic subscribers\).
> 
> I updated the PR to reflect this change :pray:

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- BadRequest is intentionally non-retry; other file/TCP failures get bounded retries because dividend files are independent and whole-topic blocking is worse.

**Evidence:** anon-2.jsonl:2678 · comment 374518385 · PR 5391 · 2023-03-03

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/subscribers/HongKongEntitlementDividendTopicSubscriber.scala`

> The ServiceLogic in dividend svc alreadymaps the scenarios it cannot handle the file to BadRequest. So we don’t want to waste time retrying for those case \(

**Evidence:** anon-2.jsonl:2678 · comment 374518385 · PR 5391 · 2023-03-03

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/subscribers/HongKongEntitlementDividendTopicSubscriber.scala`

> ’s intention\).
> 
> There could potentially still be other exceptions that not caught by ServiceLogic itself, e.g. the case of big file and the tcp connection got cut during file processing. Since we can’t reliably reproduce and fix them, we want to limit the number of retries to avoid blocking the whole topic. Each dividend file should be independent, so we don’t care about their ordering \(unlike events in other normal topic subscribers\).
> 
> I updated the PR to reflect this change :pray: 
> 
> ‌

**Evidence:** anon-2.jsonl:2678 · comment 374518385 · PR 5391 · 2023-03-03

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/subscribers/HongKongEntitlementDividendTopicSubscriber.scala`

**Explicit source context (hunk):**

> +            msg.fileDetails match {
> +              case BucketBasedFileDetails(_, objectName) =>
> +                logic
> +                  .triggerProcessingOfDividendDistribution(ProcessDividendDistributionRequest(objectName))
> +                  .withRetry({
> +                    case _: BadRequest => false
> +                    case ex =>

## A3-0822 — Recurring failure email: actual reason, event-domain coupling and direct-publish deferral

**Source stance:** suggestion

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/communication/hk/HkRecurringInvestmentFailureEmailComposer.scala; PR: Resolve INV-1135: Send email for failed recurring investments with state change info

**Concern stated in the source:** And if we add all applicable compliance block reasons \(so that we can evolve the email logic freely\), we would also bake the compliance domain to investment event domain.

* Since it might fail, we should retry, and add support to retry manually via endpoint, if needed
* You can add all the failure reasons here, but no need to think too hard, cuz it’s all on the fly - nothing is persisted
* If it gets too slow and starts impacting the main triggering flow, we can revisit moving to event processor \(or postpone further by dispatching to another kafka topic, and construct the email and publish to communication from there\)

**Source-preserving request, proposal, or question:**

> Yeah simulation only makes sense if we want to warn user about potential failure in the upcoming-recurring-investment email. For this jira, we want to include exactly the failure reason. This means the entry point to construct the email should already contain the failure reason, passed from the `RecurringInvestmentProcessor`.
> 
> 
> 
> This can be achieved via Cmd\+Evt like what you did here. However, I feel we might couple our event domain with the copy \(suitability VS risk breach\), e.g today we add CrBreach as reason, tmr copy wants to distinguish between Cat1 breach vs Cat2 breach. And if we add all applicable compliance block reasons \(so that we can evolve the email logic freely\), we would also bake the compliance domain to investment event domain. Not to mention, we would likely support this to SG too - in which case, do we want to handle SG vs HK failure reason in the event?
> 
> 
> 
> The above is not necessarily wrong, but I don’t think we know everything to decide it now. And there’s a way to postpone this decision: by publishing directly to communication in the `RecurringInvestmentProcessor`
> 
> * Since it might fail, we should retry, and add support to retry manually via endpoint, if needed
> * You can add all the failure reasons here, but no need to think too hard, cuz it’s all on the fly - nothing is persisted
> * If it gets too slow and starts impacting the main triggering flow, we can revisit moving to event processor \(or postpone further by dispatching to another kafka topic, and construct the email and publish to communication from there\)
> 
> 
> 
> `RecurringInvestmentRequestFailedEvent` with proper region-specific failure reason sounds like a good thing to me, I’m just not sure we’re ready to implement it yet.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Keep upcoming-warning simulation distinct from actual failure reason. Persisted region/compliance/copy coupling is unresolved; direct publish with bounded retry/manual endpoint is a deferral option, later task topic/event flow conditional on slowness.

**Evidence:** anon-2.jsonl:2679 · comment 369402726 · PR 5203 · 2023-02-13

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/communication/hk/HkRecurringInvestmentFailureEmailComposer.scala`

> Yeah simulation only makes sense if we want to warn user about potential failure in the upcoming-recurring-investment email. For this jira, we want to include exactly the failure reason. This means the entry point to construct the email should already contain the failure reason, passed from the `RecurringInvestmentProcessor`.
> 
> ‌
> 
> This can be achieved via Cmd\+Evt like what you did here. However, I feel we might couple our event domain with the copy \(suitability VS risk breach\), e.g today we add CrBreach as reason, tmr copy wants to distinguish between Cat1 breach vs Cat2 breach. And if we add all applicable compliance block reasons \(so that we can evolve the email logic freely\), we would also bake the compliance domain to investment event domain. Not to mention, we would likely support this to SG too - in which case, do we want to handle SG vs HK failure reason in the event?
> 
> ‌
> 
> The above is not necessarily wrong, but I don’t think we know everything to decide it now. And there’s a way to postpone this decision: by publishing directly to communication in the `RecurringInvestmentProcessor`
> 
> * Since it might fail, we should retry, and add support to retry manually via endpoint, if needed
> * You can add all the failure reasons here, but no need to think too hard, cuz it’s all on the fly - nothing is persisted
> * If it gets too slow and starts impacting the main triggering flow, we can revisit moving to event processor \(or postpone further by dispatching to another kafka topic, and construct the email and publish to communication from there\)
> 
> ‌
> 
> `RecurringInvestmentRequestFailedEvent` with proper region-specific failure reason sounds like a good thing to me, I’m just not sure we’re ready to implement it yet. 
> 
> ‌

## A3-0825 — RecurringInvestmentProcessor.scala: Can we move retry logic to `tradabilityChecker` itself, similar to complianceChecker? It’s already very cluttered here

**Source stance:** open-question

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala; PR: Resolve INV-1135: Send email for failed recurring investments with state change info

**Source-preserving request, proposal, or question:**

> Can we move retry logic to `tradabilityChecker` itself, similar to complianceChecker? It’s already very cluttered here

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2682 · comment 374499963 · PR 5203 · 2023-03-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala`

> Can we move retry logic to `tradabilityChecker` itself, similar to complianceChecker? It’s already very cluttered here
> 
> ‌

**Evidence:** anon-2.jsonl:2682 · comment 374499963 · PR 5203 · 2023-03-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala`

**Explicit source context (hunk):**

> -      actionIfValidationPassed,
> -      actionIfValidationFailed = {
> +    tradabilityChecker.isInvestmentAllowedByPlanId(investmentPlan.planId) transformWith {
> +      case Success(true) => actionIfValidationPassed
> +      case Success(false) =>
>          logger.warn(
>            s"triggerRecurringInvestments - Investment plan [${investmentPlan.planId}] is not tradable, will NOT create a recurring investment request."

## A3-0826 — RecurringInvestmentProcessor.scala: No we should only retry when it makes sense to… but it means the underlying service needs to tell you that. In this case, we build compliance service 

**Source stance:** explanation

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala; PR: Resolve INV-1135: Send email for failed recurring investments with state change info

**Concern stated in the source:** In this case, we build compliance service to tell its consumer about race condition to retry.

**Source-preserving request, proposal, or question:**

> No we should only retry when it makes sense to… but it means the underlying service needs to tell you that.
> 
> In this case, we build compliance service to tell its consumer about race condition to retry.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Related source rows 2683, 2684: Retry transient errors when signaled is preferred; bounded retry-all is temporarily tolerated.

**Evidence:** anon-2.jsonl:2683 · comment 374500532 · PR 5203 · 2023-03-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala`

**Evidence:** anon-2.jsonl:2683 · comment 374500532 · PR 5203 · 2023-03-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala`

**Explicit source context (hunk):**

> -      actionIfValidationPassed,
> -      actionIfValidationFailed = {
> +    tradabilityChecker.isInvestmentAllowedByPlanId(investmentPlan.planId) transformWith {
> +      case Success(true) => actionIfValidationPassed
> +      case Success(false) =>
>          logger.warn(
>            s"triggerRecurringInvestments - Investment plan [${investmentPlan.planId}] is not tradable, will NOT create a recurring investment request."

## A3-0827 — Bounded retry-all temporarily tolerated while underlying retryability contract evolves

**Source stance:** suggestion

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala; PR: Resolve INV-1135: Send email for failed recurring investments with state change info

**Source-preserving request, proposal, or question:**

> Having said that, as long as we don’t retry forever / repeatedly - it might be ok to retry on all exceptions for now.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Bounded retry-all temporarily tolerated, not a mandate to retry permanent errors forever; pair with2683's service-provided transient signal.
- Related source rows 2683, 2684: Retry transient errors when signaled is preferred; bounded retry-all is temporarily tolerated.

**Evidence:** anon-2.jsonl:2684 · comment 374500630 · PR 5203 · 2023-03-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala`

**Evidence:** anon-2.jsonl:2684 · comment 374500630 · PR 5203 · 2023-03-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala`

**Explicit source context (hunk):**

> -      actionIfValidationPassed,
> -      actionIfValidationFailed = {
> +    tradabilityChecker.isInvestmentAllowedByPlanId(investmentPlan.planId) transformWith {
> +      case Success(true) => actionIfValidationPassed
> +      case Success(false) =>
>          logger.warn(
>            s"triggerRecurringInvestments - Investment plan [${investmentPlan.planId}] is not tradable, will NOT create a recurring investment request."

## A3-0828 — RecurringInvestmentProcessor.scala: Oh why are we retrying again here

**Source stance:** open-question

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala; PR: Resolve INV-1135: Send email for failed recurring investments with state change info

**Source-preserving request, proposal, or question:**

> Oh why are we retrying again here

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2685 · comment 374501198 · PR 5203 · 2023-03-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala`

**Evidence:** anon-2.jsonl:2685 · comment 374501198 · PR 5203 · 2023-03-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala`

**Explicit source context (hunk):**

> -      actionIfValidationFailed = {
> +    complianceChecker.validateRecurringInvestmentRequest(investmentPlan.customerId, complianceCheckRequest) transformWith {
> +      case Success(ComplianceValidationResult(violations)) if violations.isEmpty => actionIfValidationPassed(investmentRequestIdToUse)
> +      case Success(ComplianceValidationResult(violations)) =>
>          logger.warn(
>            s"triggerRecurringInvestments - Customer [${investmentPlan.customerId}] planId [${investmentPlan.planId}] has invalid compliance check status. No recurring investments will be made."
>          )

## A3-0830 — RecurringInvestmentProcessor.scala: Ok then can we move all that to the checkers themselves? This processor should just focus on the logic I think

**Source stance:** open-question

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala; PR: Resolve INV-1135: Send email for failed recurring investments with state change info

**Source-preserving request, proposal, or question:**

> Ok then can we move all that to the checkers themselves? This processor should just focus on the logic I think

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2687 · comment 374501699 · PR 5203 · 2023-03-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala`

**Evidence:** anon-2.jsonl:2687 · comment 374501699 · PR 5203 · 2023-03-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala`

**Explicit source context (hunk):**

> -      actionIfValidationFailed = {
> +    complianceChecker.validateRecurringInvestmentRequest(investmentPlan.customerId, complianceCheckRequest) transformWith {
> +      case Success(ComplianceValidationResult(violations)) if violations.isEmpty => actionIfValidationPassed(investmentRequestIdToUse)
> +      case Success(ComplianceValidationResult(violations)) =>
>          logger.warn(
>            s"triggerRecurringInvestments - Customer [${investmentPlan.customerId}] planId [${investmentPlan.planId}] has invalid compliance check status. No recurring investments will be made."
>          )

## A3-0832 — RecurringInvestmentProcessor.scala: Yes, notification is “extra” in this flow. Let’s do it last, with retry \(inside the email helper\). Log error if exhaust all retries, and expose endp

**Source stance:** requested-change

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala; PR: Resolve INV-1135: Send email for failed recurring investments with state change info

**Source-preserving request, proposal, or question:**

> Yes, notification is “extra” in this flow. Let’s do it last, with retry \(inside the email helper\). Log error if exhaust all retries, and expose endpoint to trigger the mail manually if needed.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2689 · comment 374503818 · PR 5203 · 2023-03-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala`

**Evidence:** anon-2.jsonl:2689 · comment 374503818 · PR 5203 · 2023-03-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala`

**Explicit source context (hunk):**

> -      actionIfValidationErrored = ex => {
> -        logger.warn(s"triggerRecurringInvestments - Failure encountered when checking if plan [${investmentPlan.planId}] is not tradable", ex)
> +        for {
> +          _ <- notifyFailedInvestmentRequest(investmentPlan, dateToUse)
> +          scheduleResult <- updateNextUpcomingDateForPlan(dateToUse, investmentPlan)
> +            .map(_ => RecurringInvestmentScheduleResult(1, 0, 0, 0, 1, 0))
> +        } yield scheduleResult

## A3-0842 — HkNotificationManager.scala: Or maybe this method can just log warn and skip the customer. No point to throw?

**Source stance:** suggestion

**Context:**

> customer-impl/src/main/scala/com/endowus/silver/customer/impl/logic/HkNotificationManager.scala; PR: Feat/INV-898 pi passport expiring emails

**Source-preserving request, proposal, or question:**

> Or maybe this method can just log warn and skip the customer. No point to throw?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2700 · comment 372609347 · PR 5354 · 2023-02-24

Source path: `customer-impl/src/main/scala/com/endowus/silver/customer/impl/logic/HkNotificationManager.scala`

**Evidence:** anon-2.jsonl:2700 · comment 372609347 · PR 5354 · 2023-02-24

Source path: `customer-impl/src/main/scala/com/endowus/silver/customer/impl/logic/HkNotificationManager.scala`

**Explicit source context (hunk):**

> +          case Some(custId) => custId match {
> +            case _ :HkCustomerOfficialIdentification.NationalIdentityCard =>
> +              logger.warn(s"Unexpected customer id ${custData.customer.customerId} ID type of national ID!")
> +              Future.successful(None)
> +            case passport: HkCustomerOfficialIdentification.Passport =>
> +              Future.successful(Some(PassportDataWithCustomer(custData.customer.customerId, custData.customer.personalDetails.map(_.firstName), passport)))
> +          }

## A3-0849 — NotificationManager.scala: You can do ``` .mapAsync(2) { case (customerData, profileData) => ... } ```

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/NotificationManager.scala; PR: Resolve INV-896: Changes to publish email/platform notifs for upcoming customer vc warnings.

**Source-preserving request, proposal, or question:**

> You can do
> 
> ```
> .mapAsync(2) { case (customerData, profileData) =>
>   ...
> }
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2707 · comment 372348538 · PR 5329 · 2023-02-23

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/NotificationManager.scala`

> You can do
> 
> ```
> .mapAsync(2) { case (customerData, profileData) =>
>   ...
> }
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2707 · comment 372348538 · PR 5329 · 2023-02-23

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/NotificationManager.scala`

**Explicit source context (hunk):**

> +    val customersToNotify = customerProjectionDataJdbcRepository
> +      .findValidNonVCWithAdvisoryProfile(birthdaysBasedOnCutoffAge)
> +      .mapAsync(2) { case(customerData, profileData) =>
> +        profileData.advisoryProfile match {
> +          case NonVulnerableCustomerProfile(_, RiskProfileStatus.Valid, _, _) =>
> +            for {
> +              craSimulationResult <- simulateCraWithVcCutOffAge(customerData.customerId)

## A3-0850 — NotificationManager.scala: Looks like you don’t need for-comprehend block here

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/NotificationManager.scala; PR: Resolve INV-896: Changes to publish email/platform notifs for upcoming customer vc warnings.

**Source-preserving request, proposal, or question:**

> Looks like you don’t need for-comprehend block here

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2708 · comment 372348662 · PR 5329 · 2023-02-23

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/NotificationManager.scala`

**Evidence:** anon-2.jsonl:2708 · comment 372348662 · PR 5329 · 2023-02-23

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/NotificationManager.scala`

**Explicit source context (hunk):**

> +          case NonVulnerableCustomerProfile(_, RiskProfileStatus.Valid, _, _) =>
> +            for {
> +              craSimulationResult <- simulateCraWithVcCutOffAge(customerData.customerId)
> +
> +              filteredData <- craSimulationResult match {
> +                case _: VulnerableCustomerProfile =>
> +                  Future.successful(Some(customerData))

## A3-0878 — ServiceLogicImpl.scala: move this into the recover block of `retrieveFirstRowInDividendDistributionFile`?

**Source stance:** suggestion

**Context:**

> dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/logic/service/impl/ServiceLogicImpl.scala; PR: [TT-1503] fix(dividend): convert not found error to bad request error

**Source-preserving request, proposal, or question:**

> Let’s move this into the recover block of `retrieveFirstRowInDividendDistributionFile`?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2737 · comment 365301125 · PR 5121 · 2023-01-30

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/logic/service/impl/ServiceLogicImpl.scala`

## A3-0880 — FxRatesProjectionRepository.scala: If no streaming, then don’t need SlickSession I think

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/FxRatesProjectionRepository.scala; PR: Feat/INV-913 fx rates projection

**Source-preserving request, proposal, or question:**

> If no streaming, then don’t need SlickSession I think

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2739 · comment 354168399 · PR 4915 · 2022-12-16

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/FxRatesProjectionRepository.scala`

**Evidence:** anon-2.jsonl:2739 · comment 354168399 · PR 4915 · 2022-12-16

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/FxRatesProjectionRepository.scala`

**Explicit source context (hunk):**

> +
> +class FxRatesProjectionRepository (database: Database)(implicit ctx: ExecutionContext) {
> +
> +  private val fxRatesProjectionTable = TableQuery[FxRatesProjectionTable]
> +
> +  def findCcyPairRateByPriceDate(baseCcy: CurrencyUnit, quoteCcy: CurrencyUnit, priceDate: LocalDate): Future[Option[FxRateProjectionData]] = {
> +    database.run {

## A3-0883 — FxRatesTopicSubscriberV2.scala: This the upsert call fails, the whole future will still error, and the subscriber will retry. The `.map(_ => Done)` purely means “we are ignoring the 

**Source stance:** explanation

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/FxRatesTopicSubscriberV2.scala; PR: Feat/INV-913 fx rates projection

**Source-preserving request, proposal, or question:**

> This the upsert call fails, the whole future will still error, and the subscriber will retry. The `.map(_ => Done)` purely means “we are ignoring the result of the upsert, if it succeeds”

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2742 · comment 354168987 · PR 4915 · 2022-12-16

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/FxRatesTopicSubscriberV2.scala`

> This the upsert call fails, the whole future will still error, and the subscriber will retry. The `.map(_ => Done)` purely means “we are ignoring the result of the upsert, if it succeeds”
> 
> ‌

**Evidence:** anon-2.jsonl:2742 · comment 354168987 · PR 4915 · 2022-12-16

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/FxRatesTopicSubscriberV2.scala`

**Explicit source context (hunk):**

> +    .atLeastOnce(Flow[FxRatesMsg].mapAsync(parallelism = 1) {
> +
> +    case msg: FxRateUpdatedMsg =>
> +      fxRatesProjectionJdbcDbHandler.upsert(FxRateProjectionData(
> +        baseCcy = msg.baseCcy, quoteCcy = msg.quoteCcy, priceDate = msg.priceDate, rate = msg.fxRate
> +      )).map(_ => Done)
> +

## A3-0891 — Macwire inside Future sometimes misses subscribers; possible SlickReadside relation unproven

**Source stance:** open-question

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/AdvisoryApplication.scala; PR: Feat/INV-969 auto change VC

**Concern stated in the source:** 's testing shows that using just the above sometimes will not wire the subscribers correctly \(and now I’m wondering if the jdbc event processors using SlickReadside getting “stuck” related to this - they also follow similar pattern, i.e.

**Source-preserving request, proposal, or question:**

> Ok this looks weird, but I also don’t know why it doesn’t work with just
> 
> ```
> createCustomTopics().map(_ => {
>    wire[A]
>    wire[B]
> })
> ```
> 
>   
>  do you have any idea? 's testing shows that using just the above sometimes will not wire the subscribers correctly \(and now I’m wondering if the jdbc event processors using SlickReadside getting “stuck” related to this - they also follow similar pattern, i.e. run something first, then wire\)

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Intermittent macwire-in-Future initialization issue is unresolved; possible SlickReadside relation is speculation, not verified cause.

**Evidence:** anon-2.jsonl:2750 · comment 366320053 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/AdvisoryApplication.scala`

> Ok this looks weird, but I also don’t know why it doesn’t work with just
> 
> ```
> createCustomTopics().map(_ => {
>    wire[A]
>    wire[B]
> })
> ```

**Evidence:** anon-2.jsonl:2750 · comment 366320053 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/AdvisoryApplication.scala`

> do you have any idea?

**Evidence:** anon-2.jsonl:2750 · comment 366320053 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/AdvisoryApplication.scala`

> 's testing shows that using just the above sometimes will not wire the subscribers correctly \(and now I’m wondering if the jdbc event processors using SlickReadside getting “stuck” related to this - they also follow similar pattern, i.e. run something first, then wire\)

**Evidence:** anon-2.jsonl:2750 · comment 366320053 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/AdvisoryApplication.scala`

**Explicit source context (hunk):**

> +
> +  lazy val craExpiryDailyTriggerTopicProducerDirect: CRAExpiryDailyTriggerTopicProducerDirect = wire[CRAExpiryDailyTriggerTopicProducerDirect]
> +  lazy val vcStateChangeDailyTriggerTopicProducerDirect: VCStateChangeDailyTriggerTopicProducerDirect = wire[VCStateChangeDailyTriggerTopicProducerDirect]
> +  createCustomTopics().map(_ => for {
> +    //TODO(nate) Find better way to wire this subscribers...
> +    _ <- Future.unit
> +    _ = wire[CRAExpiryDailyTriggerTopicSubscriber]

## A3-0918 — CraManager.scala: Can just log warn and move on? Same for VC below?

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> Can just log warn and move on? Same for VC below?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2777 · comment 367135510 · PR 5109 · 2023-02-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Evidence:** anon-2.jsonl:2777 · comment 367135510 · PR 5109 · 2023-02-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Explicit source context (hunk):**

> +            forceUpdateCraExpiryDate(
> +              customerId,
> +              expiryDate,
> +              "SYSTEM",
> +              "State Change CRA Expiry Trigger"
> +            )
> +        case _: VulnerableCustomerProfile =>

## A3-0924 — CraManager.scala: If we throw, we block Kafka..

**Source stance:** observed-defect

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> If we throw, we block Kafka..

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2783 · comment 367143068 · PR 5109 · 2023-02-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Evidence:** anon-2.jsonl:2783 · comment 367143068 · PR 5109 · 2023-02-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Explicit source context (hunk):**

> +              dob = dob,
> +              latestTS = latestTS,
> +              executeDate = executeDate
> +            )
> +            _ <- if (customerExceedVCGracePeriod && customerNotRetakenCRAAfterBirthday)
> +                reassessVulnerableStatus(customerId, "SYSTEM", "State Change VC Trigger")
> +              else

## A3-0931 — HkServiceLogicImpl.scala: Oh bulk upsert for whole set of customers would be too large… either batch the source, or just upsert one by one I think…

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/HkServiceLogicImpl.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> Oh bulk upsert for whole set of customers would be too large… either batch the source, or just upsert one by one I think…

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2790 · comment 367471398 · PR 5109 · 2023-02-07

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/HkServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:2790 · comment 367471398 · PR 5109 · 2023-02-07

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/HkServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +              Future.successful(None)
> +          }
> +      }
> +      .grouped(10)
> +      .map(customers => customerProjectionDataJdbcDbHandler.bulkUpsert(customers.flatten))
> +      .runWith(Sink.ignore)
> +      .onComplete({

## A3-0972 — ServiceLogicImpl.scala: we don’t actually need this for comprehend block here if it’s just one future

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/impl/ServiceLogicImpl.scala; PR: [EN-674] feat(transaction) create an api to get transactions for a customer id with goal id and statuses filter

**Source-preserving request, proposal, or question:**

> Nit: we don’t actually need this for comprehend block here if it’s just one future

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2832 · comment 357769261 · PR 5028 · 2023-01-05

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/impl/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:2832 · comment 357769261 · PR 5028 · 2023-01-05

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +    maybeTransactionStatuses: Option[Set[TransactionStatus]]
> +  ): Future[TransactionListDto] = {
> +    val filters = List(
> +      Some(Filter("customerId", Op.Eq, customerId.toString)),
> +      mayBeGoalId.map(goalId => Filter("goalId", Op.Eq, goalId.toString)),
> +      maybeTransactionStatuses.map(transactionStatuses => Filter("status", Op.In, Json.toJson(transactionStatuses).toString))
> +    ).flatten

## A3-0975 — LagomServiceExceptionHelper.scala: I guess it’s not really required here \(and only here\)… `PrintWriter#close` will attempt to close its underlying output stream which is this `CharArr

**Source stance:** explanation

**Context:**

> silver-commons/src/main/scala/com/endowus/silver/commons/exception/LagomServiceExceptionHelper.scala; PR: [INV-956] feat(advisory)(investment)(compliance): Use ClassTag to avoid type erasure in LagomServiceExceptionHelper

**Source-preserving request, proposal, or question:**

> I guess it’s not really required here \(and only here\)… `PrintWriter#close` will attempt to close its underlying output stream which is this `CharArrayWriter`, which again has empty impl in `CharArrayWriter#close`

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2835 · comment 356181112 · PR 4979 · 2022-12-27

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/exception/LagomServiceExceptionHelper.scala`

## A3-0976 — Scala2.11 PrintWriter/CharArrayWriter no-close exception relies on noop underlying close

**Source stance:** explanation

**Context:**

> silver-commons/src/main/scala/com/endowus/silver/commons/exception/LagomServiceExceptionHelper.scala; PR: [INV-956] feat(advisory)(investment)(compliance): Use ClassTag to avoid type erasure in LagomServiceExceptionHelper

**Concern stated in the source:** But I’m making a special case here that we don’t need to call `close` at all, because `PrintWriter#close` would simply call `CharArrayWriter#close` which does nothing…

In fact, the only reason I’m still arguing with you here is because we’re on scala 2.11 which doesn’t support the `using` block \(equivalent to java’s try-with-resources\).

**Source-preserving request, proposal, or question:**

> Yes I know that. But I’m making a special case here that we don’t need to call `close` at all, because `PrintWriter#close` would simply call `CharArrayWriter#close` which does nothing…
> 
> ```java
>     /**
>      * Close the stream.  This method does not release the buffer, since its
>      * contents might still be required. Note: Invoking this method in this class
>      * will have no effect.
>      */
>     public void close() { }
> ```
> 
> 
> 
> In fact, the only reason I’m still arguing with you here is because we’re on scala 2.11 which doesn’t support the `using` block \(equivalent to java’s try-with-resources\). I don’t want to unnecessarily try-catch-finally to complicate this method further, especially when I know we don’t need it :stuck_out_tongue:

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- This is an explicit no-close special case for PrintWriter wrapping CharArrayWriter whose close is noop, with Scala2.11 lacking using. Do not generalize to resources with real cleanup.

**Evidence:** anon-2.jsonl:2836 · comment 356394341 · PR 4979 · 2022-12-28

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/exception/LagomServiceExceptionHelper.scala`

> Yes I know that. But I’m making a special case here that we don’t need to call `close` at all, because `PrintWriter#close` would simply call `CharArrayWriter#close` which does nothing…
> 
> ```java
>     /**
>      * Close the stream.  This method does not release the buffer, since its
>      * contents might still be required. Note: Invoking this method in this class
>      * will have no effect.
>      */
>     public void close() { }
> ```
> 
> ‌
> 
> In fact, the only reason I’m still arguing with you here is because we’re on scala 2.11 which doesn’t support the `using` block \(equivalent to java’s try-with-resources\). I don’t want to unnecessarily try-catch-finally to complicate this method further, especially when I know we don’t need it :stuck_out_tongue:

## A3-0977 — InstrumentMarketDataEventProcessorForMultiCcy.scala: So we keep trying until the circuit breaker resets?

**Source stance:** open-question

**Context:**

> marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/processors/InstrumentMarketDataEventProcessorForMultiCcy.scala; PR: Feat/reduce sentry noise

**Source-preserving request, proposal, or question:**

> So we keep trying until the circuit breaker resets?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2837 · comment 357230642 · PR 5011 · 2023-01-03

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/processors/InstrumentMarketDataEventProcessorForMultiCcy.scala`

**Evidence:** anon-2.jsonl:2837 · comment 357230642 · PR 5011 · 2023-01-03

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/processors/InstrumentMarketDataEventProcessorForMultiCcy.scala`

**Explicit source context (hunk):**

> -              case ex: Exception =>
> +            .recoverWith({
> +              case retryableException: CircuitBreakerOpenException =>
> +                Future.failed(retryableException)
> +              case ex =>
>                  logger.error(s"handleMonthlyChangesFxConversion failed for currency pair. From CCY: ${id.marketDataCcy}, To CCY: $toCcy", ex)
> -                Done

## A3-0983 — Missing broker virtual-account data blocks tag and may age communication past2days

**Source stance:** open-question

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentCommunicationV2EventProcessor.scala; PR: EN-120 Handle Investment Completed and Upcoming Recurring Investment emails using Comms V2

**Source-preserving request, proposal, or question:**

> we throw if `brokerAccount` has missing data for `virtualAccountNumber`, event processor is stuck until someone fix on broker svc side? And this would delay communication for all other events in same tag, potentially beyond the `dateTimeProvider.now.minusDays(2)` ?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2843 · comment 354939478 · PR 4890 · 2022-12-20

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentCommunicationV2EventProcessor.scala`

**Evidence:** anon-2.jsonl:2843 · comment 354939478 · PR 4890 · 2022-12-20

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentCommunicationV2EventProcessor.scala`

**Explicit source context (hunk):**

> +                  Locale.EN_HK -> "

**Evidence:** anon-2.jsonl:2843 · comment 354939478 · PR 4890 · 2022-12-20

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentCommunicationV2EventProcessor.scala`

**Explicit source context (hunk):**

> ",
> +                  Locale.EN_SG -> "

**Evidence:** anon-2.jsonl:2843 · comment 354939478 · PR 4890 · 2022-12-20

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentCommunicationV2EventProcessor.scala`

**Explicit source context (hunk):**

> "
> +                ),
> +                templateData = UpcomingRecurringInvestmentData(
> +                  GOAL_NAME = goal.name,
> +                  STOCK_PERCENTAGE = ratioPercentages._1.toString,
> +                  BOND_PERCENTAGE = ratioPercentages._2.toString,

## A3-1007 — NewWealthDataUploader.scala: Do you want to add a utils method to wrap future with `.withRetry(AlwaysRetryOnException, retrySettings)` instead? We always use default retry setting

**Source stance:** suggestion

**Context:**

> marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/NewWealthDataUploader.scala; PR: New wealth script

**Source-preserving request, proposal, or question:**

> Do you want to add a utils method to wrap future with `.withRetry(AlwaysRetryOnException, retrySettings)` instead?
> 
> We always use default retry settings, so I feel we don’t even need to have it injected to reduce boiler plate. Even if we do, I think let’s just inject `Config` and construct retrySettings in this `NewWealthApiHelper` instead

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2868 · comment 353194356 · PR 4893 · 2022-12-13

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/NewWealthDataUploader.scala`

## A3-1012 — Error-contract tests: missing CRA, concurrent invest retry, instrument-down propagation

**Source stance:** reported-verification

**Context:**

> None; PR: Extract common Lagom exception helper

**Source-preserving request, proposal, or question:**

> Tested in `advisory`: query CRA with invalid customerId returns expected error json, but no error logs
> 
> ```
> GET <url>
> {
>     "error_code": "CUSTOMER_NOT_FOUND",
>     "name": "com.endowus.silver.advisory.api.exceptions.AdvisorySvcException",
>     "detail": "Customer advisory profile not found"
> }
> ```
> 
> 
> 
> Tested in `investment` and `compliance`: submit concurrent invest-once
> 
> * `investment` is able to retry automatically when `compliance` returns concurrent modification error
> * no error logs on `compliance` side
> 
> ![](<url>
> Tested in `investment` and `compliance`: invest-once when `instrument` svc is down
> 
> * `investment` is able to check exception type from `compliance` and abort the request
> * error is logged on `compliance` side as TransportException due to uncaught exception
> * error is logged on `investment` side as wrapped InvestmentSvcException and propagate accordingly to caller
> 
> ```
> {
>     "error_code":"COMPLIANCE_SERVICE_ERROR",
>     "name":"com.endowus.silver.investment.api.exceptions.InvestmentSvcException",
>     "detail":"Compliance check for one-time investment for Customer[] InvestmentRequestId[] errored due to compliance service exception"
> }
> ```
> 
> ![](<url>

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Preserve invalid CRA CUSTOMER_NOT_FOUND/no-error-log; concurrent invest compliance retry/no-compliance-log; instrument-down abort with TransportException log in compliance and wrapped InvestmentSvcException log in investment.

**Evidence:** anon-2.jsonl:2874 · comment 353206494 · PR 4896 · 2022-12-13

> Tested in `advisory`: query CRA with invalid customerId returns expected error json, but no error logs
> 
> ```
> GET <url>
> {
>     "error_code": "CUSTOMER_NOT_FOUND",
>     "name": "com.endowus.silver.advisory.api.exceptions.AdvisorySvcException",
>     "detail": "Customer advisory profile not found"
> }
> ```
> 
> ‌
> 
> Tested in `investment` and `compliance`: submit concurrent invest-once
> 
> * `investment` is able to retry automatically when `compliance` returns concurrent modification error
> * no error logs on `compliance` side
> 
> ![](<url>
> Tested in `investment` and `compliance`: invest-once when `instrument` svc is down
> 
> * `investment` is able to check exception type from `compliance` and abort the request
> * error is logged on `compliance` side as TransportException due to uncaught exception
> * error is logged on `investment` side as wrapped InvestmentSvcException and propagate accordingly to caller
> 
> ```
> {
>     "error_code":"COMPLIANCE_SERVICE_ERROR",
>     "name":"com.endowus.silver.investment.api.exceptions.InvestmentSvcException",
>     "detail":"Compliance check for one-time investment for Customer[

**Evidence:** anon-2.jsonl:2874 · comment 353206494 · PR 4896 · 2022-12-13

> ] InvestmentRequestId[

**Evidence:** anon-2.jsonl:2874 · comment 353206494 · PR 4896 · 2022-12-13

> ] errored due to compliance service exception"
> }
> ```
> 
> ![](<url>
> ‌

## A3-1046 — HkServiceLogicImpl.scala: We don’t need this cuz the cmd already returns Done?

**Source stance:** open-question

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/HkServiceLogicImpl.scala; PR: Feat/INV-840 plan upsert confirmation

**Concern stated in the source:** We don’t need this cuz the cmd already returns Done?

**Source-preserving request, proposal, or question:**

> We don’t need this cuz the cmd already returns Done?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2910 · comment 349048911 · PR 4779 · 2022-11-28

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/HkServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:2910 · comment 349048911 · PR 4779 · 2022-11-28

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/HkServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +            requestedBy = request.requestedBy
> +          )
> +        )
> +    }
> +  }
>  }

## A3-1057 — KafkaTaskHelper.scala: can you guys take a quick look at this helper? I extract the retry behaviour to `FutureUtils.futureWithRetry` for reuse

**Source stance:** explanation

**Context:**

> silver-commons/src/main/scala/com/endowus/silver/commons/kafka/KafkaTaskHelper.scala; PR: [INV-814] feat(investment)(compliance)(report): Implement HkComplianceChecker for Investment service

**Source-preserving request, proposal, or question:**

> can you guys take a quick look at this helper? I extract the retry behaviour to `FutureUtils.futureWithRetry` for reuse

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2922 · comment 349063179 · PR 4777 · 2022-11-28

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/kafka/KafkaTaskHelper.scala`

**Evidence:** anon-2.jsonl:2922 · comment 349063179 · PR 4777 · 2022-11-28

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/kafka/KafkaTaskHelper.scala`

**Explicit source context (hunk):**

> -            case _ => None
> -          })
> +      FutureUtils
> +        .futureWithRetry(
> +          fut,
> +          shouldRetryOnException = {
> +            case _: UnsafeForRetryException => false

## A3-1080 — CraCategoryMatcher.scala: This one is more like utils method, so let’s put it in companion object? Also we don’t need Future?

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/cra/CraCategoryMatcher.scala; PR: Feat/INV-672 dashboard and warnings

**Source-preserving request, proposal, or question:**

> This one is more like utils method, so let’s put it in companion object? Also we don’t need Future?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2946 · comment 346477942 · PR 4671 · 2022-11-17

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/cra/CraCategoryMatcher.scala`

## A3-1090 — Projection transient retryWARN versus persistent lag threshold1hr and Sentry flooding

**Source stance:** explanation

**Context:**

> dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/brokerAccount/processors/AutoSellDownDividendProcessor.scala; PR: [EN-311] feat(dividend) publish new email request for dividend

**Concern stated in the source:** Retry is successful, and no one would bother about it
* persistent: exception will keep throwing and event processor would be stuck and keep retrying.

**Source-preserving request, proposal, or question:**

> Imagine if exception happens:
> 
> * one-off: exception will be thrown normally, and event processor retries by itself. Event processor would log a WARN log I believe. Retry is successful, and no one would bother about it
> * persistent: exception will keep throwing and event processor would be stuck and keep retrying. We should set up monitoring for event processor lag \(with appropriate lag threshold, currently it’s 1hr for all\) to catch it. If we log error here, sentry will be flooded

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- One-off retry/WARN versus persistent-stuck lag monitoring (then1hr threshold); error log would flood Sentry. Preserve as scoped logging/monitoring rationale.

**Evidence:** anon-2.jsonl:2956 · comment 339565318 · PR 4506 · 2022-10-21

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/brokerAccount/processors/AutoSellDownDividendProcessor.scala`

> Imagine if exception happens:
> 
> * one-off: exception will be thrown normally, and event processor retries by itself. Event processor would log a WARN log I believe. Retry is successful, and no one would bother about it
> * persistent: exception will keep throwing and event processor would be stuck and keep retrying. We should set up monitoring for event processor lag \(with appropriate lag threshold, currently it’s 1hr for all\) to catch it. If we log error here, sentry will be flooded
> 
> ‌

## A3-1096 — BaseServiceLogicImpl.scala: You can just use `=` if not returning a future.. It’s equivalent to `Future#map`

**Source stance:** suggestion

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala; PR: [EN-231] feat(goal) create edge api for getting redeemable goals

**Source-preserving request, proposal, or question:**

> You can just use `=` if not returning a future.. It’s equivalent to `Future#map`

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2962 · comment 344414078 · PR 4570 · 2022-11-10

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:2962 · comment 344414078 · PR 4570 · 2022-11-10

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +  }
> +
> +  private def isRedeemable(planIds: String): Future[Boolean] = {
> +    if (planIds.isEmpty) {
> +      Future.successful(false)
> +    } else {
> +      for {

## A3-1099 — BaseServiceLogicImpl.scala: The 2 calls to trading and marketdata are independent of each other. If time is a concern, we can call them in parallel too, instead of sequential lik

**Source stance:** suggestion

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala; PR: [EN-231] feat(goal) create edge api for getting redeemable goals

**Source-preserving request, proposal, or question:**

> The 2 calls to trading and marketdata are independent of each other. If time is a concern, we can call them in parallel too, instead of sequential like this

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2965 · comment 344422782 · PR 4570 · 2022-11-10

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:2965 · comment 344422782 · PR 4570 · 2022-11-10

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +    if (planIds.isEmpty) {
> +      Future.successful(false)
> +    } else {
> +      for {
> +        redemptionPlanRedeemableFlags <- redemptionService.getRedemptionPlanRedeemableStatusList(planIds).invoke()
> +      } yield redemptionPlanRedeemableFlags.exists(s => s.isRedeemable)
> +    }

## A3-1110 — ModifyPlanAcknowledgementsLogic.scala: Don’t need for-comprehension block if you have only one future

**Source stance:** requested-change

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/ModifyPlanAcknowledgementsLogic.scala; PR: [INV-675] Added modify acks with testcase

**Source-preserving request, proposal, or question:**

> Don’t need for-comprehension block if you have only one future

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:2977 · comment 343433852 · PR 4605 · 2022-11-07

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/ModifyPlanAcknowledgementsLogic.scala`

## A3-1126 — SimulateTradingRestrictionLogic.scala: Surprise surprise, it’s not lazy :grimacing:

**Source stance:** observed-defect

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/SimulateTradingRestrictionLogic.scala; PR: Feat/INV-732 PI check simulation confirm

**Source-preserving request, proposal, or question:**

> Surprise surprise, it’s not lazy :grimacing:

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2997 · comment 343545246 · PR 4619 · 2022-11-07

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/SimulateTradingRestrictionLogic.scala`

**Evidence:** anon-2.jsonl:2997 · comment 343545246 · PR 4619 · 2022-11-07

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/SimulateTradingRestrictionLogic.scala`

**Explicit source context (hunk):**

> customerId: UUID
>    )(request: TradingSimulationRestrictionRequest): Future[TradingSimulationRestrictionResponse] = {
>      for {
> -      craDetailsResponse <- advisoryService.getCraDetails(customerId).invoke()
>        targetAllocation <- extractTargetAllocation(request)

## A3-1134 — QueryTradingRestrictionLogic.scala: Right ok, so we lookup for all plans, and the entity has initial empty state if no acks. Should be able to lazy this, and only lookup acks if plan has

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/QueryTradingRestrictionLogic.scala; PR: [INV-669] State change impacted plans

**Source-preserving request, proposal, or question:**

> Right ok, so we lookup for all plans, and the entity has initial empty state if no acks.
> 
> Should be able to lazy this, and only lookup acks if plan has recurring schedule?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:3005 · comment 342007987 · PR 4577 · 2022-11-01

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/QueryTradingRestrictionLogic.scala`

## A3-1155 — SupportTradingRestrictionLogic.scala: Will move this to background task, return Future\[Done\] when we implement Slack integration. In this version, simply collect data and return in respo

**Source stance:** explanation

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/SupportTradingRestrictionLogic.scala; PR: Feat/INV-557 buy earmark recon

**Source-preserving request, proposal, or question:**

> Will move this to background task, return Future\[Done\] when we implement Slack integration.
> 
> In this version, simply collect data and return in response payload

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3027 · comment 342571506 · PR 4597 · 2022-11-03

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/SupportTradingRestrictionLogic.scala`

**Evidence:** anon-2.jsonl:3027 · comment 342571506 · PR 4597 · 2022-11-03

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/SupportTradingRestrictionLogic.scala`

**Explicit source context (hunk):**

> +      )
> +  }
> +
> +  override def reportBuyEarmarksWithPotentialIssue(): Future[EarmarkReconciliationReport] = {
> +    for {
> +      (maybeStuckBuyEarmarks, maybeOrphanedBuyEarmarks) <- buyEarmarkRepository
> +        .streamAllInvestmentBuyEarmarks()

## A3-1162 — StatementDataGenerator has documentId+statement after PDF; avoid topic relookup for comm

**Source stance:** suggestion

**Context:**

> report-impl/src/main/scala/com/endowus/silver/report/impl/subscribers/DocumentTopicSubscriber.scala; PR: [EN-313] publish v2 email request for monthly statements

**Source-preserving request, proposal, or question:**

> Report’s service StatementDataGenerator has the following:
> 
> ```scala
> for {
>   documentId <- createPdfFileWithAppServer(statementInfo)
>   maybeDocumentId = Some(UUID.fromString(documentId))
>   _ <- statementDbHandler.insert(statementInfo.copy(documentId = maybeDocumentId)).recover {
>     case ex =>
>       throw UnsafeForRetryException(s"Statement insert for customer ${request.customerId} failed!!", ex)
>   }
> 
>   fileCreatedResponse = CreateCustomerStatementResponse(
>     status = StatementStatusEnum.CREATED,
>     documentId = maybeDocumentId,
>     statementInfo = Some(statementInfo)
>   )
>   _ = {
>     logger.info(s"Finished creating statement of type [${request.statementType}] for customer [${statementInfo.customerId}]...")
>   }
> } yield fileCreatedResponse
> ```
> 
> 
> 
> documentId in L2 is only returned after document is created I believe. That means here we have both the documentId \+ statement data. I think we can just publish to communication svc from here, rather than another than another `DocumentTopicSubscriber` in report, and lookup the statement again

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Document ID is returned only after PDF creation; proposed communication publish in StatementDataGenerator reuses ID+statement rather than DocumentTopicSubscriber relookup. Preserve UnsafeForRetryException on statement insert.

**Evidence:** anon-2.jsonl:3035 · comment 339340137 · PR 4547 · 2022-10-20

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/subscribers/DocumentTopicSubscriber.scala`

> Report’s service StatementDataGenerator has the following:
> 
> ```scala
> for {
>   documentId <- createPdfFileWithAppServer(statementInfo)
>   maybeDocumentId = Some(UUID.fromString(documentId))
>   _ <- statementDbHandler.insert(statementInfo.copy(documentId = maybeDocumentId)).recover {
>     case ex =>
>       throw UnsafeForRetryException(s"Statement insert for customer ${request.customerId} failed!!", ex)
>   }
> 
>   fileCreatedResponse = CreateCustomerStatementResponse(
>     status = StatementStatusEnum.CREATED,
>     documentId = maybeDocumentId,
>     statementInfo = Some(statementInfo)
>   )
>   _ = {
>     logger.info(s"Finished creating statement of type [${request.statementType}] for customer [${statementInfo.customerId}]...")
>   }
> } yield fileCreatedResponse
> ```
> 
> ‌
> 
> documentId in L2 is only returned after document is created I believe. That means here we have both the documentId \+ statement data. I think we can just publish to communication svc from here, rather than another than another `DocumentTopicSubscriber` in report, and lookup the statement again

## A3-1177 — ChargeApplication.scala: Hmm if lazy val, and not injected anywhere, I don’t think these will get wired at all?

**Source stance:** open-question

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/ChargeApplication.scala; PR: invest services split

**Source-preserving request, proposal, or question:**

> Hmm if lazy val, and not injected anywhere, I don’t think these will get wired at all?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3050 · comment 333385528 · PR 4304 · 2022-09-27

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/ChargeApplication.scala`

**Evidence:** anon-2.jsonl:3050 · comment 333385528 · PR 4304 · 2022-09-27

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/ChargeApplication.scala`

**Explicit source context (hunk):**

> -  lazy val feeEstimator = wire[CustomerFeeEstimator]
> +  val planTopicSubscriber: PlanTopicSubscriber = wire[PlanTopicSubscriber]
> +  val goalTopicSubscriber: GoalTopicSubscriber = wire[GoalTopicSubscriber]
> +  lazy val planTimeSeriesTopicSubscriber: PlanTimeSeriesTopicSubscriber = wire[PlanTimeSeriesTopicSubscriber]
> +  val fxRatesTopicSubscriber: FxRatesTopicSubscriber = wire[FxRatesTopicSubscriber]
> +  val voucherWalletTopicSubscriber: VoucherWalletTopicSubscriber = wire[VoucherWalletTopicSubscriber]
> +  val redemptionTopicSubscriber: RedemptionTopicSubscriber = wire[RedemptionTopicSubscriber]

## A3-1205 — TradingRestrictionLogic.scala: This will not wait for the future to complete. And we wouldn’t know if it fails either…

**Source stance:** observed-defect

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/TradingRestrictionLogic.scala; PR: Feat/INV-560 recurring and ack persistence

**Source-preserving request, proposal, or question:**

> This will not wait for the future to complete. And we wouldn’t know if it fails either…

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3079 · comment 337484977 · PR 4477 · 2022-10-13

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/TradingRestrictionLogic.scala`

**Evidence:** anon-2.jsonl:3079 · comment 337484977 · PR 4477 · 2022-10-13

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/TradingRestrictionLogic.scala`

**Explicit source context (hunk):**

> -      }else {
> -        Future.successful(tradingRestriction.Blocked(Set(ContainsComplexProductsWithoutAcknowledgement)))
> +      if (restrictionErrors.isEmpty) {
> +        validateCr(request, customerId, targetAllocation.map(s => s._1.instrumentId -> s._2), advisoryProfile, requiresCat2Validation = false)
> +      } else {
> +        Future.successful(tradingRestriction.Blocked(restrictionErrors.toSet))
>        }

## A3-1220 — MarketDataUploader.scala: Why do we need to separate this future?

**Source stance:** open-question

**Context:**

> marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; PR: Feat/INV-613 add annual yield marketdata

**Source-preserving request, proposal, or question:**

> Why do we need to separate this future?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3095 · comment 337781639 · PR 4486 · 2022-10-14

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Evidence:** anon-2.jsonl:3095 · comment 337781639 · PR 4486 · 2022-10-14

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (hunk):**

> +    val mstarApiIdFut = getMstarApiId(instrumentId)
> +    val instrumentCcyFut = getInstrumentCcy(instrumentId)
> +
> +    val annualYieldInstrumentCcyFut: Future[(MstarAnnualYield, CurrencyUnit)] = for {
> +      id <- mstarApiIdFut
> +      instrumentCcy <- instrumentCcyFut
> +      annualYield <- mstarApiService.getAnnualYield(id, instrumentCcy)

## A3-1221 — MarketDataUploader.scala: Yeah, I can’t see the benefit of this being in separate for-comprehension block

**Source stance:** suggestion

**Context:**

> marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; PR: Feat/INV-613 add annual yield marketdata

**Source-preserving request, proposal, or question:**

> Yeah, I can’t see the benefit of this being in separate for-comprehension block

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3096 · comment 337782621 · PR 4486 · 2022-10-14

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Evidence:** anon-2.jsonl:3096 · comment 337782621 · PR 4486 · 2022-10-14

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (hunk):**

> +    val mstarApiIdFut = getMstarApiId(instrumentId)
> +    val instrumentCcyFut = getInstrumentCcy(instrumentId)
> +
> +    val annualYieldInstrumentCcyFut: Future[(MstarAnnualYield, CurrencyUnit)] = for {
> +      id <- mstarApiIdFut
> +      instrumentCcy <- instrumentCcyFut
> +      annualYield <- mstarApiService.getAnnualYield(id, instrumentCcy)

## A3-1223 — InstrumentManager.scala: Wanna take this chance to refactor this into for-comprehension instead of async await?

**Source stance:** open-question

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/InstrumentManager.scala; PR: adds fund inception date/distribution status/is complex to instrument

**Source-preserving request, proposal, or question:**

> Wanna take this chance to refactor this into for-comprehension instead of async await?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3098 · comment 336600016 · PR 4455 · 2022-10-10

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/InstrumentManager.scala`

**Evidence:** anon-2.jsonl:3098 · comment 336600016 · PR 4455 · 2022-10-10

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/InstrumentManager.scala`

**Explicit source context (hunk):**

> createdInstrument
>    }
>  
> -  def createFundInstrument(request: UpsertFundInstrumentRequest): Future[InstrumentInfoDto] = async {
> -    val isin = request.id
> -    val mstarId = MstarApiId(isin, MstarApiIdType.ISIN)
> -    val isMstarCompatibleInstrument = request.isMstarCompatibleInstrument.getOrElse(true)
> -    val (name, idMap) = if (isMstarCompatibleInstrument) {
> -      val basicFundInfoFut = mstarApiService.getFundShareClassBasicInfo(mstarId)
> -      val fundBasicInfo = await(basicFundInfoFut)
> -      val idMap = Map(
> -        InstrumentIdType.MSTAR_ID -> fundBasicInfo.mstarId,
> -        InstrumentIdType.ISIN -> fundBasicInfo.isin
> +  def createFundInstrument(request: UpsertFundInstrumentRequ

## A3-1264 — Release-earmark subscriber serial1 is conservative preference, not required ordering proof

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/HkInvestmentTopicSubscriber.scala; PR: Feat/INV-551 release earmark

**Source-preserving request, proposal, or question:**

> In this subscriber, we only care to release earmark, and once released, we don’t care about it anymore. So parallelism here should be ok I think, but I guess to be on safe side \(since it won’t be significantly better anyway\), we can stick to processing 1 at a time

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Earmark-release subscriber ordering not semantically needed after release, but serial1 preferred conservatively for little performance benefit; do not generalize serial requirement.

**Evidence:** anon-2.jsonl:3145 · comment 335700694 · PR 4377 · 2022-10-06

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/HkInvestmentTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:3145 · comment 335700694 · PR 4377 · 2022-10-06

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/HkInvestmentTopicSubscriber.scala`

**Explicit source context (hunk):**

> +  implicit ec: ExecutionContext,
> +  mat: Materializer
> +) extends LazyLogging {
> +  investmentService.investmentRequestTopic.subscribe.atLeastOnce(Flow[InvestmentRequestMsg].mapAsync(parallelism = 1) {
> +    case msg: InvestmentRequestSubmittedExternallyMsg =>
> +      processEarmarkRelease(msg.customerId)(
> +        msg.goalId,

## A3-1268 — BrokerCashTransactionTopicSubscriberV2.scala: If we throw here, this subscriber will stuck on this message

**Source stance:** observed-defect

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/BrokerCashTransactionTopicSubscriberV2.scala; PR: INV-553 feat: Deposit and InterestReceived Transaction Subscriber

**Concern stated in the source:** If we throw here, this subscriber will stuck on this message

**Source-preserving request, proposal, or question:**

> If we throw here, this subscriber will stuck on this message

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3149 · comment 334763362 · PR 4360 · 2022-10-03

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/BrokerCashTransactionTopicSubscriberV2.scala`

**Evidence:** anon-2.jsonl:3149 · comment 334763362 · PR 4360 · 2022-10-03

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/BrokerCashTransactionTopicSubscriberV2.scala`

**Explicit source context (hunk):**

> +        }
> +
> +        _ <- if (deletedTransactionMaybe.isEmpty) {
> +          logger.error(s"Transaction [${msg.transactionId}] is not of the expected type [${expectedTxType}]...")
> +          Future.successful(Done)
> +        } else if (transaction.statusDetails.isInstanceOf[DeletedStatusDetails]) {
> +          Future.successful(Done)

## A3-1284 — ChargeApplication.scala: This one looks strange. How is it possible that this one is lazy val in SG today :open_mouth: I guess because it’s wired in `ServiceLogicImpl` ? Seem 

**Source stance:** open-question

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/ChargeApplication.scala; PR: splits charge into sg vs hk

**Concern stated in the source:** I guess because it’s wired in `ServiceLogicImpl` ?

**Source-preserving request, proposal, or question:**

> This one looks strange. How is it possible that this one is lazy val in SG today :open_mouth: 
> 
> I guess because it’s wired in `ServiceLogicImpl` ? Seem dangerous to me… I think we should not use lazy here, since we definitely want to listen to timeseries always?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3166 · comment 333447633 · PR 4347 · 2022-09-27

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/ChargeApplication.scala`

**Evidence:** anon-2.jsonl:3166 · comment 333447633 · PR 4347 · 2022-09-27

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/ChargeApplication.scala`

**Explicit source context (hunk):**

> -  lazy val feeEstimator = wire[CustomerFeeEstimator]
> +  val planTopicSubscriber: PlanTopicSubscriber = wire[PlanTopicSubscriber]
> +  val goalTopicSubscriber: GoalTopicSubscriber = wire[GoalTopicSubscriber]
> +  lazy val planTimeSeriesTopicSubscriber: PlanTimeSeriesTopicSubscriber = wire[PlanTimeSeriesTopicSubscriber]
> +  val fxRatesTopicSubscriber: FxRatesTopicSubscriber = wire[FxRatesTopicSubscriber]
> +  val voucherWalletTopicSubscriber: VoucherWalletTopicSubscriber = wire[VoucherWalletTopicSubscriber]
> +  val redemptionTopicSubscriber: RedemptionTopicSubscriber = wire[RedemptionTopicSubscriber]

## A3-1293 — ConcentrationRiskValidator.scala: This duplicate pattern matching on request type seems to suggest we should break down by type earlier. Example for the simulation flow: ```scala def v

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/cr/ConcentrationRiskValidator.scala; PR: Feat/INV-486 add goal earmark

**Concern stated in the source:** This duplicate pattern matching on request type seems to suggest we should break down by type earlier.

**Source-preserving request, proposal, or question:**

> This duplicate pattern matching on request type seems to suggest we should break down by type earlier.
> 
> Example for the simulation flow:
> 
> ```scala
>   def validateSimulation(customerId: UUID, advisoryRiskProfile: RiskProfile, liquidNetWorth: BigDecimal)(
>     request: TradingSimulationRestrictionRequest,
>     requiresCat2Validation: Boolean
>   ): Future[Boolean] = {
>     val investmentValueCalculatorFn: CustomerTradingEarmarkManagerState => Future[Map[RiskLevel, BigDecimal]] = existingEarmarkState =>
>       request match {
>         ...
>       }
> 
>     validationSimulation(customerId, advisoryRiskProfile, liquidNetWorth)(investmentValueCalculatorFn, requiresCat2Validation)
>   }
> 
>   private def validationSimulation(customerId: UUID, advisoryRiskProfile: RiskProfile, liquidNetWorth: BigDecimal)(
>     investmentValueCalculatorFn: CustomerTradingEarmarkManagerState => Future[Map[RiskLevel, BigDecimal]],
>     requiresCat2Validation: Boolean
>   ): Future[Boolean] = {
>     for {
>       existingEarmarkState <- refProvider.getCustomerTradingEarmarkManagerEntity(customerId).ask(GetCustomerTradingEarmarksCmd)
>       investmentValuesByRiskLevel <- investmentValueCalculatorFn(existingEarmarkState)
>     } yield {
>       validateCat1CrLimit(liquidNetWorth, investmentValuesByRiskLevel) &&
>       (!requiresCat2Validation || validateCat2CrLimit(advisoryRiskProfile)(liquidNetWorth, investmentValuesByRiskLevel))
>     }
>   }
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Preserve function-injected simulation skeleton and exact CAT1&&(!requiresCAT2||CAT2) condition; pattern-match request once outside.

**Evidence:** anon-2.jsonl:3175 · comment 333432324 · PR 4344 · 2022-09-27

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/cr/ConcentrationRiskValidator.scala`

> This duplicate pattern matching on request type seems to suggest we should break down by type earlier.
> 
> Example for the simulation flow:
> 
> ```scala
>   def validateSimulation(customerId: UUID, advisoryRiskProfile: RiskProfile, liquidNetWorth: BigDecimal)(
>     request: TradingSimulationRestrictionRequest,
>     requiresCat2Validation: Boolean
>   ): Future[Boolean] = {
>     val investmentValueCalculatorFn: CustomerTradingEarmarkManagerState => Future[Map[RiskLevel, BigDecimal]] = existingEarmarkState =>
>       request match {
>         ...
>       }
> 
>     validationSimulation(customerId, advisoryRiskProfile, liquidNetWorth)(investmentValueCalculatorFn, requiresCat2Validation)
>   }
> 
>   private def validationSimulation(customerId: UUID, advisoryRiskProfile: RiskProfile, liquidNetWorth: BigDecimal)(
>     investmentValueCalculatorFn: CustomerTradingEarmarkManagerState => Future[Map[RiskLevel, BigDecimal]],
>     requiresCat2Validation: Boolean
>   ): Future[Boolean] = {
>     for {
>       existingEarmarkState <- refProvider.getCustomerTradingEarmarkManagerEntity(customerId).ask(GetCustomerTradingEarmarksCmd)
>       investmentValuesByRiskLevel <- investmentValueCalculatorFn(existingEarmarkState)
>     } yield {
>       validateCat1CrLimit(liquidNetWorth, investmentValuesByRiskLevel) &&
>       (!requiresCat2Validation || validateCat2CrLimit(advisoryRiskProfile)(liquidNetWorth, investmentValuesByRiskLevel))
>     }
>   }
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:3175 · comment 333432324 · PR 4344 · 2022-09-27

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/cr/ConcentrationRiskValidator.scala`

**Explicit source context (hunk):**

> +    instrumentWeights: InstrumentWeights,
> +    customerId: UUID,
> +    advisoryRiskProfile: RiskProfile,
> +    liquidNetWorth: BigDecimal
> +  )(
> +    request: TradingRestrictionRequest,
> +    requiresCat2Validation: Boolean

## A3-1294 — ConcentrationRiskValidator.scala: This way, for confirmation flow, the skeleton private method would accept 2 functions returning Future: * one for the investment values * another for 

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/cr/ConcentrationRiskValidator.scala; PR: Feat/INV-486 add goal earmark

**Source-preserving request, proposal, or question:**

> This way, for confirmation flow, the skeleton private method would accept 2 functions returning Future:
> 
> * one for the investment values
> * another for the register earmarks if success
> 
> 
> 
> Then we pattern match by request type outside, once, and return tuple of the functions
> 
> ```scala
>     val blah: (CustomerTradingEarmarkManagerState => Future[Map[RiskLevel, BigDecimal]], () => Future[Done]) = request match {
>       case GoalCreateSimulationRestrictionRequest(targetInstrumentWeights, initialInvestmentAmount, _) =>
>         initialInvestmentAmount.filter(_ > 0) match {
>           case Some(amount) =>
>             (
>               existingEarmarkState => Future.successfule(Map()),
>               () => Future.successful(Done)
>             )
>           case None =>
>             throw ComplianceServiceException(
>               ComplianceServiceErrorType.InternalError,
>               s"Invalid state. Request [$request] not applicable for ConcentrationRisk validation"
>             )
>         }
> 
>       case _ =>
>         throw ComplianceServiceException(
>           ComplianceServiceErrorType.NotImplementedError,
>           s"Unsupported TradingRestrictionRequest of type ${request.getClass.getSimpleName}"
>         )
>     }
> ```
> 
> 
> 
> Need to name / extract this properly of course :grimacing:

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Confirmation skeleton takes investment-values function and success-only earmark-registration function; code is illustrative proposal including placeholders.

**Evidence:** anon-2.jsonl:3176 · comment 333435934 · PR 4344 · 2022-09-27

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/cr/ConcentrationRiskValidator.scala`

> This way, for confirmation flow, the skeleton private method would accept 2 functions returning Future:
> 
> * one for the investment values
> * another for the register earmarks if success
> 
> ‌
> 
> Then we pattern match by request type outside, once, and return tuple of the functions
> 
> ```scala
>     val blah: (CustomerTradingEarmarkManagerState => Future[Map[RiskLevel, BigDecimal]], () => Future[Done]) = request match {
>       case GoalCreateSimulationRestrictionRequest(targetInstrumentWeights, initialInvestmentAmount, _) =>
>         initialInvestmentAmount.filter(_ > 0) match {
>           case Some(amount) =>
>             (
>               existingEarmarkState => Future.successfule(Map()),
>               () => Future.successful(Done)
>             )
>           case None =>
>             throw ComplianceServiceException(
>               ComplianceServiceErrorType.InternalError,
>               s"Invalid state. Request [$request] not applicable for ConcentrationRisk validation"
>             )
>         }
> 
>       case _ =>
>         throw ComplianceServiceException(
>           ComplianceServiceErrorType.NotImplementedError,
>           s"Unsupported TradingRestrictionRequest of type ${request.getClass.getSimpleName}"
>         )
>     }
> ```
> 
> ‌
> 
> Need to name / extract this properly of course :grimacing:

**Evidence:** anon-2.jsonl:3176 · comment 333435934 · PR 4344 · 2022-09-27

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/cr/ConcentrationRiskValidator.scala`

**Explicit source context (hunk):**

> +    instrumentWeights: InstrumentWeights,
> +    customerId: UUID,
> +    advisoryRiskProfile: RiskProfile,
> +    liquidNetWorth: BigDecimal
> +  )(
> +    request: TradingRestrictionRequest,
> +    requiresCat2Validation: Boolean

## A3-1358 — CustomerAdvisoryProfileEntity.scala: Yup. Switched to another exception type for concurrent modification, and retry on it in the subscriber

**Source stance:** explanation

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileEntity.scala; PR: [INV-349] feat(advisory): Trigger CRA VC status reassessment when customer update PersonalDetails

**Source-preserving request, proposal, or question:**

> Yup. Switched to another exception type for concurrent modification, and retry on it in the subscriber

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3244 · comment 329773426 · PR 4209 · 2022-09-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileEntity.scala`

**Evidence:** anon-2.jsonl:3244 · comment 329773426 · PR 4209 · 2022-09-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileEntity.scala`

**Explicit source context (hunk):**

> +              ctx.done
> +
> +            case initializedState: Initialized =>
> +              if (
> +                initializedState.craQuestionnaireVersion != cmd.craQuestionnaireVersion ||
> +                  initializedState.craCalculationMatrixVersion != cmd.craCalculationMatrixVersion ||
> +                  initializedState.annualIncome != cmd.annualIncome ||

## R-3336 — PlanTimeSeriesSubscriber: proposed mapAsync(1) without throttle before finding the unawaited simulation

**Source stance:** suggestion

**Context:**

> projection-impl/src/main/scala/com/endowus/silver/projection/impl/subscribers/PlanTimeSeriesSubscriberForLatestPlanMvTable.scala; PR 3767: projection service kafka message throttling optimization

**Source-preserving request, proposal, or question:**

> [incidental identifier omitted] [incidental identifier omitted] 
> 
> Did we check the execution speed for the jdbc persistence? I would think the main bottleneck for consumption speed from kafka here is due to this throttling, not because we were calling mapAsync with parallelism = 1 previously.
> 
> ‌
> 
> From what I observed so far, I reckon we should be able to use mapAsync with parallelism = 1, but remove the throttling, and it would be much faster without any extra complication.
> 
> ‌
> 
> We would not overly spam the pg, since mapAsync will only move on next message after current jdbc persistence returns. And kafka topic is backpressured by nature - messages only arrive if consumer calls poll.
> 
> ‌

**Conditions and limits:**

- Read together: the throttle-removal suggestion is followed by discovery of an unawaited simulation call and a separate-topic proposal. It is not a settled rule to remove throttling. Source rows: anon-2.jsonl:3336, anon-2.jsonl:3337, anon-2.jsonl:3338.
- Only incidental reviewer mentions and customer/account UUID literals are omitted in the displayed source wording; symbols, predicates, dates, thresholds, and alternatives are retained.

**Evidence:** anon-2.jsonl:3336 · comment 313172358 · PR 3767 · 2022-07-01

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/subscribers/PlanTimeSeriesSubscriberForLatestPlanMvTable.scala`

>  
> 
> Did we check the execution speed for the jdbc persistence? I would think the main bottleneck for consumption speed from kafka here is due to this throttling, not because we were calling mapAsync with parallelism = 1 previously.
> 
> ‌
> 
> From what I observed so far, I reckon we should be able to use mapAsync with parallelism = 1, but remove the throttling, and it would be much faster without any extra complication.
> 
> ‌
> 
> We would not overly spam the pg, since mapAsync will only move on next message after current jdbc persistence returns. And kafka topic is backpressured by nature - messages only arrive if consumer calls poll.
> 
> ‌

## R-3337 — safeRenewProjectionForCustomer is started with a value binding and not awaited

**Source stance:** explanation

**Context:**

> projection-impl/src/main/scala/com/endowus/silver/projection/impl/subscribers/PlanTimeSeriesSubscriberForLatestPlanMvTable.scala; PR 3767: projection service kafka message throttling optimization

**Source-preserving request, proposal, or question:**

> Ah I missed this line in the processing logic - which does not wait for simulation call to return
> 
> ```
> _ = multiCcySimulationBatchManager.safeRenewProjectionForCustomer(msg.customerId) 
> ```
> 
> ‌
> 
> Ok this makes sense now :thumbsup: 

**Conditions and limits:**

- Read together: the throttle-removal suggestion is followed by discovery of an unawaited simulation call and a separate-topic proposal. It is not a settled rule to remove throttling. Source rows: anon-2.jsonl:3336, anon-2.jsonl:3337, anon-2.jsonl:3338.

**Evidence:** anon-2.jsonl:3337 · comment 313175068 · PR 3767 · 2022-07-01

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/subscribers/PlanTimeSeriesSubscriberForLatestPlanMvTable.scala`

## R-3338 — Decouple MV draining from simulation with a separate retry/throttle/conflate topic proposal

**Source stance:** open-question

**Context:**

> projection-impl/src/main/scala/com/endowus/silver/projection/impl/subscribers/PlanTimeSeriesSubscriberForLatestPlanMvTable.scala; PR 3767: projection service kafka message throttling optimization

**Source-preserving request, proposal, or question:**

> Ah good find. Without your provided context, I thought we want parallel as much as possible, but do not want to spam the simulation service, hence the throttling to protect.
> 
> ‌
> 
> If we care about draining the MV messages fast, and ok to have projection out of sync with MV , does it make sense to dispatch the simulation service call to a separate topic? Then we can retry, throttle, conflate it independently?
> 
> For example, throttle idk X messages per Y seconds \(Y is appropriate to processing time of simulation\), and then conflate the planIds in that batch, so that we don’t unnecessarily renew, etc

**Conditions and limits:**

- Read together: the throttle-removal suggestion is followed by discovery of an unawaited simulation call and a separate-topic proposal. It is not a settled rule to remove throttling. Source rows: anon-2.jsonl:3336, anon-2.jsonl:3337, anon-2.jsonl:3338.

**Evidence:** anon-2.jsonl:3338 · comment 313179722 · PR 3767 · 2022-07-01

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/subscribers/PlanTimeSeriesSubscriberForLatestPlanMvTable.scala`

## R-3406 — Unit is like void, hence everything it mappable to Unit. And by extension, every Future\[Blah\] to mappable to Future\[Unit\]. We normally return Future\[a

**Source stance:** explanation

**Context:**

> dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/brokerAccount/processors/BrokerAccountDividendsJdbcEventProcessor.scala; PR 3299: changes to use cassandra read side

**Source-preserving request, proposal, or question:**

> Unit is like void, hence everything it mappable to Unit. And by extension, every Future\[Blah\] to mappable to Future\[Unit\].
> 
> We normally return Future\[akka.Done\] if we just want to indicate the future completes, but does not return any value.
> 
> If you still want to return nothing \(aka Unit\), then use `yield ()`. Unit is a type that has only one valid value, which is `()`

**Evidence:** anon-2.jsonl:3406 · comment 293158203 · PR 3299 · 2022-04-07

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/brokerAccount/processors/BrokerAccountDividendsJdbcEventProcessor.scala`

## R-3420 — `FeeGenerator#generatePlanFeeForFullRedemption` is not “safe” and would propagate any exception. Unlike `FeeGenerator#safeGeneratePlansFeeForCustomer` whic

**Source stance:** explanation

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/subscribers/RedemptionTopicSubscriber.scala; PR 3227: Access fee fixes

**Source-preserving request, proposal, or question:**

> `FeeGenerator#generatePlanFeeForFullRedemption` is not “safe” and would propagate any exception. Unlike `FeeGenerator#safeGeneratePlansFeeForCustomer` which would catch all exception, and return an error response, then this code would check and throw exception again.

**Evidence:** anon-2.jsonl:3420 · comment 287421009 · PR 3227 · 2022-03-15

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/subscribers/RedemptionTopicSubscriber.scala`

## R-3449 — This already returns `Future[Done]` so we don’t need this for comprehend at all? Also for timing, would you like to give `TimeUtils.TimedLogger` a try? You

**Source stance:** suggestion

**Context:**

> projection-impl/src/main/scala/com/endowus/silver/projection/impl/ProjectionServiceImpl.scala; PR 3155: Feat/projection svc multiccy batch manager

**Source-preserving request, proposal, or question:**

> This already returns `Future[Done]` so we don’t need this for comprehend at all?
> 
> Also for timing, would you like to give `TimeUtils.TimedLogger` a try?
> 
> You can use it like this
> 
> ```scala
> logger.logTime("renewProjectionForAllV2") {
>   multiCcySimulationBatchManager.renewProjectionsForAll
> }
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:3449 · comment 284843163 · PR 3155 · 2022-03-03

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/ProjectionServiceImpl.scala`

## R-3450 — Since we are already in Future scope here, I normally find it better to return `Future.failed(BadRequest())` instead Also let’s add some error message, rat

**Source stance:** suggestion

**Context:**

> projection-impl/src/main/scala/com/endowus/silver/projection/impl/ProjectionServiceImpl.scala; PR 3155: Feat/projection svc multiccy batch manager

**Source-preserving request, proposal, or question:**

> Since we are already in Future scope here, I normally find it better to return `Future.failed(BadRequest())` instead
> 
> Also let’s add some error message, rather than blank

**Conditions and limits:**

- The Future.failed suggestion is later qualified: throwing in this transformation has the same effect; the preference is personal style in an existing Future scope. Source rows: anon-2.jsonl:3450, anon-2.jsonl:3453, anon-2.jsonl:3454.

**Evidence:** anon-2.jsonl:3450 · comment 284843541 · PR 3155 · 2022-03-03

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/ProjectionServiceImpl.scala`

## R-3454 — Future.failed versus throw in transform is a personal preference with the same effect

**Source stance:** suggestion

**Context:**

> projection-impl/src/main/scala/com/endowus/silver/projection/impl/ProjectionServiceImpl.scala; PR 3155: Feat/projection svc multiccy batch manager

**Source-preserving request, proposal, or question:**

> So both will calls `transform` which perform the execution as a `Try` in a try catch block.
> 
> ‌
> 
> If we throw, the code path will involve the whole try catch, whereas if we use `Future.failed` it will just return the exception as it.
> 
> ‌
> 
> I guess for us, this doesn’t matter too much. Personally I just feel using `Future.failed` more naturally when we are already in a future scope. Both have same effect.

**Conditions and limits:**

- The Future.failed suggestion is later qualified: throwing in this transformation has the same effect; the preference is personal style in an existing Future scope. Source rows: anon-2.jsonl:3450, anon-2.jsonl:3453, anon-2.jsonl:3454.

**Evidence:** anon-2.jsonl:3454 · comment 285098929 · PR 3155 · 2022-03-04

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/ProjectionServiceImpl.scala`

## R-3455 — Maybe we don’t need parallelism = 2 here, since it’s always same entity

**Source stance:** suggestion

**Context:**

> rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/processors/RebateDistributionEventProcessor.scala; PR 3103: Fix Rebate service

**Source-preserving request, proposal, or question:**

> Maybe we don’t need parallelism = 2 here, since it’s always same entity

**Conditions and limits:**

- This is a short source statement; its complete referent may depend on the historical diff or surrounding thread. Do not infer a missing requirement.

**Evidence:** anon-2.jsonl:3455 · comment 282166672 · PR 3103 · 2022-02-23

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/processors/RebateDistributionEventProcessor.scala`

## R-3501 — Proposal to recover force-rebalance failure after successful TAA update because a later topic message can trigger rebalance

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/GoalModifyConfirmationBehaviour.scala; PR 3019: SILVER-11923: Factors goal modify summary/confirmation

**Source-preserving request, proposal, or question:**

> This force rebalance thing - if it fails, do we really want to return error to FE, even though goal’s TAA is actually successfully updated?  
>   
> I’m thinking we probably should recover this future, to log and silent the error…
> 
> Rebalance service will eventually receive `PlanTargetAssetAllocationUpdatedMsg`  and trigger rebalance then \(if still not trigger by this force call\)

**Evidence:** anon-2.jsonl:3501 · comment 278484200 · PR 3019 · 2022-02-09

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/GoalModifyConfirmationBehaviour.scala`

## R-3554 — We don’t need this? As parallelism is local to mapAsync only

**Source stance:** requested-change

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RebateDistributionTopicSubscriber.scala; PR 2798: changes endpoint to fix the rebate transactions and changes transaction service to consume in sequence

**Source-preserving request, proposal, or question:**

> We don’t need this? As parallelism is local to mapAsync only

**Conditions and limits:**

- This is a short source statement; its complete referent may depend on the historical diff or surrounding thread. Do not infer a missing requirement.

**Evidence:** anon-2.jsonl:3554 · comment 270244198 · PR 2798 · 2021-12-31

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RebateDistributionTopicSubscriber.scala`

## R-3556 — If you prefer Exception instead, because say you expect caller to always call with valid ID… then code is little cleaner to read if we return Future.failed

**Source stance:** open-question

**Context:**

> projection-impl/src/main/scala/com/endowus/silver/projection/impl/db/jdbc/portfolioStats/PortfolioStatsJdbcRepository.scala; PR 2807: Feat/projection svc portfolio stats jdbc

**Source-preserving request, proposal, or question:**

> If you prefer Exception instead, because say you expect caller to always call with valid ID… then code is little cleaner to read if we return Future.failed\(NotFound\(\)\)

**Evidence:** anon-2.jsonl:3556 · comment 270149593 · PR 2807 · 2021-12-30

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/db/jdbc/portfolioStats/PortfolioStatsJdbcRepository.scala`

## R-3558 — Portfolio stats exact-ID lookup and filter lookup both produce a List response

**Source stance:** suggestion

**Context:**

> projection-impl/src/main/scala/com/endowus/silver/projection/impl/ProjectionServiceImpl.scala; PR 2807: Feat/projection svc portfolio stats jdbc

**Source-preserving request, proposal, or question:**

> Maybe something like this?
> 
> ```scala
> for {
>   stats <- (portfolioId, effectiveDate, statsCcy) match {
>     case (Some(pid), Some(date), Some(ccy)) => portfolioStatsJdbcRepository.findById(pid, date, ccy).map(_.toSeq)
>     case _ => portfolioStatsJdbcRepository.findByFilter(portfolioId, effectiveDate, statsCcy)
>   }
> } yield stats.map(PortfolioStats.toDto).toList
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:3558 · comment 270161114 · PR 2807 · 2021-12-30

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/ProjectionServiceImpl.scala`

## R-3566 — Scala syntax question: Since you use `val syncFut`, `.runWith(Sink.ignore)` would already trigger the fire-and-forget? So we don’t need this whole for-comp

**Source stance:** open-question

**Context:**

> marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/MarketDataServiceImpl.scala; PR 2790: Feat/SILVER-10779 multiccy monthly changes

**Source-preserving request, proposal, or question:**

> Scala syntax question:   
> Since you use `val syncFut`, `.runWith(Sink.ignore)` would already trigger the fire-and-forget?
> 
> So we don’t need this whole for-comprehension block, and can simply return `Future.success(Done)`?

**Evidence:** anon-2.jsonl:3566 · comment 269767987 · PR 2790 · 2021-12-28

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/MarketDataServiceImpl.scala`

## R-3568 — Another Scala syntax question: isn’t it better to return Future.failed\(exception\) here instead of throwing?

**Source stance:** open-question

**Context:**

> marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/InstrumentMonthlyChangeJdbcBasedFxConverter.scala; PR 2790: Feat/SILVER-10779 multiccy monthly changes

**Source-preserving request, proposal, or question:**

> Another Scala syntax question: isn’t it better to return Future.failed\(exception\) here instead of throwing?

**Evidence:** anon-2.jsonl:3568 · comment 269768965 · PR 2790 · 2021-12-28

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/InstrumentMonthlyChangeJdbcBasedFxConverter.scala`

## R-3581 — Parallel confirmation safeguards rely on UI validation and rare FE-invalid requests in this flow

**Source stance:** explanation

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/goalcreate/GoalCreateConfirmationBehaviour.scala; PR 2734: SILVER-10755: Refactor Satellite

**Source-preserving request, proposal, or question:**

> So our UI already prevents invalid requests going through. This validation call is just the final safeguard. If we ever throw validation error, it should be reported as bug to FE.
> 
> That’s why calling them in parallel here would be ok, and hopefully save a little bit of time, for most of the time.

**Evidence:** anon-2.jsonl:3581 · comment 268059290 · PR 2734 · 2021-12-17

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/goalcreate/GoalCreateConfirmationBehaviour.scala`

## R-3587 — Goal modify futures are constructed sequentially and tested as three dependent steps

**Source stance:** reported-verification

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/GoalModifyConfirmationBehaviour.scala; PR 2697: SILVER-10548: Implement GoalModifyConfirmation for Income

**Source-preserving request, proposal, or question:**

> The futures are created sequentially. So we will do these 3 step by step. I have tests for those cases too

**Evidence:** anon-2.jsonl:3587 · comment 266219213 · PR 2697 · 2021-12-09

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/GoalModifyConfirmationBehaviour.scala`

